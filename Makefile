PY=python3
COV=coverage
MAIN=app.main
TEST=app.test.run_tests
SOURCES=app/bot/

.PHONY: test

install:
	pip install --no-cache-dir -r requirements.txt

run:
	$(PY) -m $(MAIN)

test:
	$(PY) -m $(TEST)

coverage:
	$(COV) run -m --source=$(SOURCES) $(TEST)
	$(COV) report -m
	