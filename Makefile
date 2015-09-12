.PHONY: clean pep8 lint test

clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*.sqlite' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

pep8:
	flake8 src/core

lint:
	pylint -E src/core

test:
	nosetests --with-isolation

help:
	@echo "Available targets:"
	@echo "- clean       Clean up the source directory"
	@echo "- pep8        Check style with flake8"
	@echo "- lint        Check style with pylint"
	@echo "- test        Run tests"
