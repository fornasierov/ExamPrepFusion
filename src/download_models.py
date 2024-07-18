from transformers import pipeline
from config.config import Config

config = Config()

for model_name in config.models:
    pipeline(
        config.task,
        model=model_name,
        framework=config.framework,
        cache_dir=config.cache_dir,
    )

print("Models downloaded successfully!")
