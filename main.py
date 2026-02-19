from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("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"))

@app.get("/")
def home():
    return {"message": "Profile Bridge Backend Live 🚀"}

@app.post("/generate")
async def generate(data: dict):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a viral social media script writer."},
            {"role": "user", "content": f"""
                Niche: {data['niche']}
                Audience: {data['audience']}
                Topic: {data['description']}
                Write short viral script + caption + hashtags.
            """}
        ]
    )

    return {"content": response.choices[0].message.content}
