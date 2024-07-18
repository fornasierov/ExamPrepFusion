from transformers import pipeline
from src.config import Config

config = Config()

for model_name in config.models_to_download:
    pipeline(
        config.task,
        model=model_name,
        framework=config.framework,
        cache_dir=config.cache_dir,
    )

print("Models downloaded successfully!")
