import os, sys


class Config:
    models_to_download = [
        "bert-base-multilingual-cased",
    ]
    model_to_use = models_to_download[0]
    cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_cache/")
    framework = "pt"
    task = "summarization"

config = Config()
print(config.cache_dir)