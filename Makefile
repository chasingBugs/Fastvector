SRC_CORE=fastvector
SRC_TEST=tests
SRC_BENCHMARKS=benchmarks

PIP=pip
PYTHON=python

help:
	@echo "Available commands:"
	@echo "test 					- run tests"
	@echo "test-coverage 			- run tests and code coverage"
	@echo "test-coverage-html			- run tests, code coverage and create html"
	@echo "benchmark 				- perform benchmark tests"

test:
	$(PYTHON) -m pytest $(SRC_TEST)

test-coverage:
	$(PYTHON) -m pytest --cov $(SRC_CORE) $(SRC_TEST)
	$(PYTHON) -m codecov

test-coverage-html:
	$(PYTHON) -m pytest --cov $(SRC_CORE) $(SRC_TEST) --cov-report=html

benchmark:
	$(PYTHON) benchmarks/test_clipping.py