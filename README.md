# Rate Limiter for APIs


API throttling function implemented using FastAPI and third-party component fastapi-ratelimiter. Set the API to no more than 100 requests within 1 minute as required, otherwise an error will be raised.

And fastapi-ratelimiter component relies on the Redis service

使用FastAPI 和第三方组件fastapi-ratelimiter实现的API节流功能的API，按照要求设置API 1分钟内不超过100次请求，否则报错
其中fastapi-ratelimiter 组件依赖Redis服务

Usage:
```shell
# Use Redis Server default setting:localhost:6379
pipenv shell
pip install -r requirements.txt
python main.py 

```

