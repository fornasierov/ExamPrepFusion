from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline
from src.api.models import summarizer

router = APIRouter()


class ExamPrepRequest(BaseModel):
    """
    Create request payload for summarization.
    """

    guidelines: list[str]


@router.post("/summarize/")
def summarize_prep(
    request: ExamPrepRequest,
    max_length: int = 130,
    min_length: int = 30,
    do_sample: bool = False,
) -> dict:
    """
    Summarize exam preparation guidelines.
    """
    combined_text = " ".join(request.guidelines)
    summary = summarizer(
        combined_text, max_length=max_length, min_length=min_length, do_sample=do_sample
    )
    return {"summary": summary[0]["summary_text"]}
