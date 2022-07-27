PYTHON ?= python3
PYTHON_PIP ?= $(PYTHON) -m pip
PYTHON_PIP_TOOLS_VERSION_SPECIFIER ?= >=6.1.0
PYTHON_PIP_TOOLS_SRC_FILES ?= requirements.in

.PHONY: python-deps-compile
python-deps-compile: $(patsubst %,python-deps-compile-%,$(PYTHON_PIP_TOOLS_SRC_FILES))
python-deps-compile: ## Compile Python dependency manifests

python-deps-compile-%:
	pip-compile --quiet "$(*)"

.PHONY: python-deps-sync-check
python-deps-sync-check: $(patsubst %,python-deps-sync-check-%,$(PYTHON_PIP_TOOLS_SRC_FILES))
python-deps-sync-check: ## Check that compiled Python dependency manifests are up-to-date with their sources

python-deps-sync-check-%: python-deps-compile-%
	@# Replace file extension of source Python dependency manifest (.in)
	@# with file extension of compiled Python dependency manifest (.txt).
	git diff --exit-code -- "$(*:.in=.txt)"

.PHONY: python-pip-tools-install
python-pip-tools-install: ## Install Pip Tools
	$(PYTHON_PIP) install 'pip-tools$(PYTHON_PIP_TOOLS_VERSION_SPECIFIER)'
