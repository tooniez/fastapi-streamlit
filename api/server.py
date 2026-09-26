from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import BaseModel
import time
from collections import defaultdict


app = FastAPI()

origins = ["http://localhost:11434"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, limit: int = 10, window: int = 60):
        super().__init__(app)
        self.limit = limit
        self.window = window
        self.requests = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        now = time.time()
        key = request.client.host if request.client else "unknown"
        timestamps = self.requests[key]
        # Remove timestamps outside the window
        timestamps[:] = [ts for ts in timestamps if now - ts < self.window]
        if len(timestamps) >= self.limit:
            return JSONResponse({
                "error": "Rate limit exceeded",
                "status_code": 429
            }, status_code=429)
        timestamps.append(now)
        response = await call_next(request)
        return response


app.add_middleware(RateLimiterMiddleware)


class DemoPostData(BaseModel):
    data: str


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}


@app.post("/demo_post")
async def demo_post(post_data: DemoPostData):
    return {"message": f"Received data: {post_data.data}"}
