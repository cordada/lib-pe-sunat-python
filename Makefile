SHELL = /usr/bin/env bash -e -o pipefail

# Python
PYTHON = python3
PYTHON_PIP = $(PYTHON) -m pip
PYTHON_PIP_VERSION_SPECIFIER = ~=22.1.2
PYTHON_SETUPTOOLS_VERSION_SPECIFIER = ~=59.4.0
PYTHON_WHEEL_VERSION_SPECIFIER = ~=0.37.1
PYTHON_VIRTUALENV_DIR = lib-pe-sunat.pyenv
PYTHON_PIP_TOOLS_VERSION_SPECIFIER = ~=6.8.0
PYTHON_PIP_TOOLS_SRC_FILES = requirements.in requirements-dev.in

# Black
BLACK = black --config .black.cfg.toml

# Mypy
MYPY_CACHE_DIR = $(CURDIR)/.mypy_cache

# Coverage.py
COVERAGE = coverage
COVERAGE_TEST_RCFILE = $(CURDIR)/.coveragerc.test.ini
COVERAGE_TEST_DATA_FILE = $(CURDIR)/.test.coverage

# Tox
TOXENV ?= py310
TOX_WORK_DIR = $(CURDIR)/.tox

# Test Reports
TEST_REPORT_DIR = $(CURDIR)/test_reports

# Python Package Building
PYTHON_PKG_BUILD_DIR = $(CURDIR)/build
PYTHON_PKG_DIST_DIR = $(CURDIR)/dist

include make/_common/help.mk
include make/python.mk

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "$@: Read README.md"
	@echo
	@$(MAKE) -s help-tasks

.PHONY: clean
clean: clean-build
clean: ## Delete temporary files, logs, cached files, build artifacts, etc.
	find . -iname __pycache__ -type d -prune -exec $(RM) -r {} \;
	find . -iname '*.py[cod]' -delete

	$(RM) -r "$(MYPY_CACHE_DIR)"
	$(RM) -r "$(COVERAGE_TEST_DATA_FILE)"
	$(RM) -r "$(TEST_REPORT_DIR)"

.PHONY: clean-build
clean-build:
	$(RM) -r "$(PYTHON_PKG_BUILD_DIR)"
	$(RM) -r "$(PYTHON_PKG_DIST_DIR)"

.PHONY: clean-all
clean-all: clean
clean-all: ## Delete (almost) everything that can be reconstructed later
	find . -iname '*.egg-info' -type d -prune -exec $(RM) -r {} \;

	$(RM) -r "$(TOX_WORK_DIR)"

.PHONY: install
install: install-deps
install: ## Install
	$(PYTHON_PIP) install --editable .
	$(PYTHON_PIP) check

.PHONY: install-dev
install-dev: install-deps-dev
install-dev: ## Install for development
	$(PYTHON_PIP) install --editable .
	$(PYTHON_PIP) check

.PHONY: install-deps
install-deps: python-pip-install python-setuptools-install python-wheel-install
install-deps: ## Install dependencies
	$(PYTHON_PIP) install -r requirements.txt
	$(PYTHON_PIP) check

.PHONY: install-deps-dev
install-deps-dev: install-deps
install-deps-dev: python-pip-tools-install
install-deps-dev: ## Install dependencies for development
	$(PYTHON_PIP) install -r requirements-dev.txt
	$(PYTHON_PIP) check

.PHONY: build
build: ## Build Python package
	$(PYTHON) setup.py build

.PHONY: dist
dist: build
dist: ## Create Python package distribution
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel

.PHONY: lint
lint: ## Run linters
	flake8
	mypy
	isort --check-only .
	$(PYTHON) setup.py check --metadata --strict
	$(BLACK) --check .

.PHONY: lint-fix
lint-fix: ## Fix lint errors
	$(BLACK) .
	isort .

.PHONY: test
test: ## Run tests
	$(PYTHON) -m tox -e "$(TOXENV)"

.PHONY: test-coverage
test-coverage: TOXENV = coverage
test-coverage: export COVERAGE_RCFILE = $(COVERAGE_TEST_RCFILE)
test-coverage: export COVERAGE_FILE = $(COVERAGE_TEST_DATA_FILE)
test-coverage: test
test-coverage: ## Run tests and measure code coverage

.PHONY: test-coverage-report
test-coverage-report: export COVERAGE_RCFILE = $(COVERAGE_TEST_RCFILE)
test-coverage-report: export COVERAGE_FILE = $(COVERAGE_TEST_DATA_FILE)
test-coverage-report: ## Run tests, measure code coverage, and generate reports
	$(COVERAGE) report
	$(COVERAGE) html

.PHONY: deploy
deploy: ## Deploy or publish
	$(PYTHON) -m twine check --strict "$(PYTHON_PKG_DIST_DIR)/*"

	$(PYTHON) -m twine upload --verbose "$(PYTHON_PKG_DIST_DIR)/*"
