dev:
	git push dev master
flake:
	flake8 pythonpackages/*.py
push:
	git push heroku master
pip:
	pip install -r requirements.txt
