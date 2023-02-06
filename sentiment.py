from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
translate = pipeline('translation', "Helsinki-NLP/opus-mt-ru-en")

@app.get("/")
async def root():
    return translate("Практическое задание №3")