SHELL = /usr/bin/env bash -e -o pipefail

# Sources Root
SOURCES_ROOT = $(CURDIR)/src

# Python
PYTHON = python3
PYTHON_PIP = $(PYTHON) -m pip
PYTHON_PIP_VERSION_SPECIFIER = $(shell \
	grep -E '^pip==.+' --no-filename --only-matching --no-messages -- requirements{,-dev}.{txt,in} \
	| head -n 1 | sed 's/^pip//' \
)
PYTHON_SETUPTOOLS_VERSION_SPECIFIER = $(shell \
	grep -E '^setuptools==.+' --no-filename --only-matching --no-messages -- requirements{,-dev}.{txt,in} \
	| head -n 1 | sed 's/^setuptools//' \
)
PYTHON_WHEEL_VERSION_SPECIFIER = $(shell \
	grep -E '^wheel==.+' --no-filename --only-matching --no-messages -- requirements{,-dev}.{txt,in} \
	| head -n 1 | sed 's/^wheel//' \
)
PYTHON_VIRTUALENV_DIR = lib-pe-sunat.pyenv
PYTHON_PIP_TOOLS_VERSION_SPECIFIER = $(shell \
	grep -E '^pip-tools==.+' --no-filename --only-matching --no-messages -- requirements{,-dev}.{txt,in} \
	| head -n 1 | sed 's/^pip-tools//' \
)
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
lint: FLAKE8_FILES = *.py "$(SOURCES_ROOT)"
lint: ISORT_FILES = *.py "$(SOURCES_ROOT)"
lint: BLACK_SRC = *.py "$(SOURCES_ROOT)"
lint: ## Run linters
	flake8 $(FLAKE8_FILES)
	mypy
	isort --check-only $(ISORT_FILES)
	$(PYTHON) setup.py check --metadata --strict
	$(BLACK) --check $(BLACK_SRC)

.PHONY: lint-fix
lint-fix: BLACK_SRC = *.py "$(SOURCES_ROOT)"
lint-fix: ISORT_FILES = *.py "$(SOURCES_ROOT)"
lint-fix: ## Fix lint errors
	$(BLACK) $(BLACK_SRC)
	isort $(ISORT_FILES)

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
	$(COVERAGE) xml
	$(COVERAGE) html

.PHONY: deploy
deploy: ## Deploy or publish
	$(PYTHON) -m twine check --strict "$(PYTHON_PKG_DIST_DIR)/*"

	$(PYTHON) -m twine upload --verbose "$(PYTHON_PKG_DIST_DIR)/*"
