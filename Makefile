PY=python3
MAIN=app.main
TEST=app.test.run_tests
.PHONY: test

run:
	$(PY) -m $(MAIN)

test:
	$(PY) -m $(TEST)
	