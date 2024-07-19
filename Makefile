install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

download_models:
	python -m src.utils.download_models

test:
	python -m pytest tests/*.py

format:	
	black src/*.py src/*/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py src/*.py src/*/*.py

refactor: format lint

deploy:
	#deploy goes here
		
ci_all: install format lint test
