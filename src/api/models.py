from transformers import pipeline
from src.config import Config

config = Config()

summarizer = pipeline(
    task=config.task,
    model=config.model_to_use,
    framework=config.framework,
)
