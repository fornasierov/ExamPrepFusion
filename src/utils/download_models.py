from transformers import pipeline
from src.config import Config

config = Config()

for model_name in config.models_to_download:
    pipeline(
        config.task,
        model=model_name,
        framework=config.framework,
    )

print("Models downloaded successfully!")
