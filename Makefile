install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv application_test.py
	python application_test.py

lint:
	pylint --disable=R,C application.py

deploy:
	echo "Deploying app"
	eb init -r us-east-2 -p python-3.7 flask-auto-deploy
	eb deploy flask-auto-deploy-env

all: install lint test 
