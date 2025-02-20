import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

deep_seek_api_key = os.getenv("DEEPSEEK_API")

# print(deep_seek_api_key)

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=deep_seek_api_key,
)

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
      "content": "Give me one cat fact"
    }
  ]
)
print(completion.choices[0].message.content)