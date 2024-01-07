# =====================================================================================
# HELPERS
# =====================================================================================

## help: print this help message
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /'

.PHONY: confirm
confirm:
	@echo -n 'Are you sure? [y/N]' && read ans && [ $${ans:-N} = y ]

# =====================================================================================
# REDIS
# =====================================================================================

## redis: start redis server
.PHONY: redis
redis:
	docker run --rm -it --name my-redis -p 6379:6379 redis

## redis/cli: start redis client
.PHONY: redis/cli
redis/cli:
	redis-cli -h localhost -p 6379

# =====================================================================================
# VIRTUAL ENVIRONMENT MANAGEMENT
# =====================================================================================

## venv: create a virtual environment using pyenv-virtualenv
.PHONY: venv
venv: confirm
	@echo 'Creating virtual environment...'
	pyenv virtualenv 3.10.13 $$(basename $$(pwd))
	pyenv local $$(basename $$(pwd))
	python -m pip install --upgrade pip

## venv/install: install dependencies from requirements files
.PHONY: venv/install
venv/install: confirm
	@echo 'Installing dependencies...'
	python -m pip install -r requirements.txt

## venv/freeze: freeze requirements into requirements/constraints.txt
.PHONY: venv/freeze
venv/freeze: confirm
	@echo 'Freezing dependencies...'
	python -m pip freeze --exclude-editable > requirements/constraints.txt

## venv/clean: remove all dependencies from the virtual environment
.PHONY: venv/clean
venv/clean: confirm
	@echo 'Removing all installed packages...'
	python -m pip freeze | xargs -I {} python -m pip uninstall -y {}

## venv/delete: delete virtual environment
.PHONY: venv/delete
venv/delete: confirm
	@echo 'Deleting virtual environment...'
	pyenv virtualenv-delete -f $$(basename $$(pwd))
	rm -f .python-version

# =====================================================================================
# QUALITY CONTROL
# =====================================================================================

## audit: format code, sort imports, check types and test all code
.PHONY: audit
audit:
	@echo 'Formatting code...'
	python -m ruff format app tests 
	@echo 'Sorting imports...'
	python -m ruff check --select I --fix app tests
	@echo 'Checking types...'
	python -m mypy app tests
	@echo 'Running tests...'
	python -m pytest -v
