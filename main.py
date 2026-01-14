from typing import Union
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    client = MongoClient(
        "mongodb+srv://alfredprincipe_db_user:9KO2U3oxFbJIsDPr@cluster0.crtg7na.mongodb.net/?appName=Cluster0"
    )
    try:
        db = client["fastapi3"]
        yield db
    finally:
        client.close()


class PostBase(BaseModel):
    tittle: str = Field(..., min_length=1, max_length=255)
    content: str


@app.post("/post/create-json-data")
async def create_one_post_json_data(post: PostBase, db=Depends(get_db)):
    new_post = {"title": post.title, "content": post.content, "created": datetime.now()}

    result = db["post"].insert_one(new_post)
    created_post = db["post"].find_one({"_id": result.inserted_id})

    return {
        "id": str(created_post["_id"]),
        "title": created_post["title"],
        "content": created_post["content"],
        "created": created_post["created"].isoformat(),
    }
class object(Objetct)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
