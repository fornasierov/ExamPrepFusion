import os, sys


class Config:
    models_to_download = [
        "bert-base-multilingual-cased",
    ]
    model_to_use = models_to_download[0]
    framework = "pt"
    task = "summarization"
