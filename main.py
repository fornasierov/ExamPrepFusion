from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()


class ExamPrepRequest(BaseModel):
    """
    Create request payload for summarization.
    """

    guidelines: list[str]


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


@app.post("/summarize/")
def summarize_prep(
    request: ExamPrepRequest,
    max_length: int = 130,
    min_length: int = 30,
    do_sample: bool = False,
) -> str:
    """
    Summarize exam preparation guidelines.
    """
    combined_text = " ".join(request.guidelines)
    summary = summarizer(
        combined_text, max_length=max_length, min_length=min_length, do_sample=do_sample
    )
    return {"summary": summary[0]["summary_text"]}


@app.get("/")
def read_root() -> dict:
    """
    Welcome message.
    """
    return {"message": "Welcome to Exam Prep Summarization API!"}
