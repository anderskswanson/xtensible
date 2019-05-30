PY=python3
MAIN=app/main.py
TEST=app/test/run_tests.py
.PHONY: test

run:
	$(PY) $(MAIN)

test:
	$(PY) $(TEST)
	