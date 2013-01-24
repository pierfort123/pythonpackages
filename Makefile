flake:
	flake8 pythonpackages/*.py
push:
	git push heroku master
pip:
	pip install -r requirements.txt
