import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("KIMI_API_KEY"),
    base_url='https://api.moonshot.cn/v1'
)

MODEL = "kimi-latest"