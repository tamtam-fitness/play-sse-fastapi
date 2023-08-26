import os
import openai
from fastapi import FastAPI, Body
from sse_starlette.sse import EventSourceResponse
from pydantic import BaseModel
import uvicorn
import json

openai.api_key = os.getenv("OPENAI_API_KEY")


class Query(BaseModel):
    query: str


# https://devdojo.com/bobbyiliev/how-to-use-server-sent-events-sse-with-fastapi
async def get_answer(query: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        stream=True,
        messages=[
            {
                "role": "user",
                "content": f"{query}"
            }
        ],
    )

    for item in response:
        try:
            content = item['choices'][0]['delta']['content']
        except:
            content = ""
        yield {"data": json.dumps({"content": content})}
    yield {"data": "[DONE]"}


app = FastAPI()


@app.post("/streaming/ask")
async def ask_stream(query: Query):
    return EventSourceResponse(get_answer(query.query))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
