test: flake8 mypy black isort pytest

flake8:
	flake8

mypy:
	mypy -p wac
	mypy -p test

black:
	black wac test -l 79 --check --diff --color

isort:
	isort . --diff --check

pytest:
	pytest test --cov --cov-report=html --cov-report=term
