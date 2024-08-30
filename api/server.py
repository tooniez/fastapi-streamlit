from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Sample route
@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}


class DemoPostData(BaseModel):
    data: str


@app.post("/demo_post")
async def demo_post(post_data: DemoPostData):
    return {"message": f"Received data: {post_data.data}"}
