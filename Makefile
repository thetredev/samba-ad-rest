.DEFAULT_GOAL := install

clean:
	@rm -rf dist
	@rm -rf .venv

build: clean
	@python3 -m venv .venv
	@. .venv/bin/activate
	@pip install samba-ad-rest[dev]
	@python3 -m build

install: build
	@pip install dist/*.whl
