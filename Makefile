SHELL = /usr/bin/env bash -e -o pipefail

# Python
PYTHON = python3
PYTHON_PIP = $(PYTHON) -m pip
PYTHON_PIP_TOOLS_VERSION_SPECIFIER = ~=6.8.0
PYTHON_PIP_TOOLS_SRC_FILES = requirements.in requirements-dev.in

include make/python.mk
