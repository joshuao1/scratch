from typing import Union

from fastapi import FastAPI

from openai import OpenAI

import os
from dotenv import load_dotenv

from pydantic import BaseModel

class Item(BaseModel):
    name: str

load_dotenv()

deep_seek_api_key = os.getenv("DEEPSEEK_API")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=deep_seek_api_key,
)

# completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },
#   extra_body={},
#   model="deepseek/deepseek-chat:free",
#   messages=[
#     {
#       "role": "user",
#       "content": "Give me another cat fact"
#     }
#   ]
# )
# print(completion.choices[0].message.content)

app = FastAPI()

@app.get("/")
def read_root():
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model="deepseek/deepseek-chat:free",
        messages=[
            {
            "role": "user",
            "content": "Give me another cat fact"
            }
        ]
)
    return {completion.choices[0].message.content}


@app.post("/question/")
async def create_item(item: Item):
    print(item.name)
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model="deepseek/deepseek-chat:free",
        messages=[
            {
            "role": "user",
            "content": item.name
            }
        ])
    return {completion.choices[0].message.content}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}