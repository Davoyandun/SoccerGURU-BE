create-dev-env:
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip3 install -r requirements.txt

run-app:
	python3 runner.py
