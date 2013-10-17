pre:
	flake8 pythonpackages/*.py
	bin/python setup.py test
