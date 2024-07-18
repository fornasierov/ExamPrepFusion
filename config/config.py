import os, sys


class Config:
    models = [
        "bert-base-multilingual-cased",
    ]
    cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_cache")
    framework = "pt"
    task = "summarization"
