import asyncio
from datetime import datetime

import aioredis
import uvicorn
from fastapi import FastAPI, Depends
from starlette.responses import JSONResponse

from fastapi_ratelimiter import RateLimited, RedisDependencyMarker
from fastapi_ratelimiter.strategies import BucketingRateLimitStrategy

app = FastAPI()
redis = aioredis.from_url("redis://localhost")


@app.get(
    "/", response_class=JSONResponse,
    dependencies=[
        Depends(RateLimited(BucketingRateLimitStrategy(rate="100/60s")))
    ]
)
async def handle_test_endpoint():
    await asyncio.sleep(0.001)
    return {
        "hello": "world",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }


app.dependency_overrides[RedisDependencyMarker] = lambda: redis

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=80, reload=True)
