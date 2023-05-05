# Rate Limiter for APIs


- API throttling function implemented using [FastAPI](https://github.com/tiangolo/fastapi) and third-party component [fastapi-ratelimiter](https://github.com/GLEF1X/fastapi-ratelimiter). Set the API to no more than 100 requests within 1 minute as required, otherwise an error will be reported. The fastapi-ratelimiter component relies on Redis service




Usage:
```shell
# Use Redis Server default setting:localhost:6379
pipenv shell
pip install -r requirements.txt
python main.py 

```

