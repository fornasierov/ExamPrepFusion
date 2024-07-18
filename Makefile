install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

download_models:
	python -m src.utils.download_models

test:
	python -m pytest -vv --cov=src tests/*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py src/*.py

refactor: format lint

deploy:
	#deploy goes here
		
ci_all: install lint test format deploy
