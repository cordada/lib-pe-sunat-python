# PE-SUNAT Python Library

This is a Python library for the *Superintendencia Nacional de Aduanas y de Administración
Tributaria* (SUNAT) of *Perú*.


## Dashboard

### Development

| VCS Branch | Deployment Environment | VCS Repository | CI/CD Status |
| ---------- | ---------------------- | -------------- | ------------ |
| `develop` | Staging | [GitHub](https://github.com/cordada/lib-pe-sunat-python/tree/develop) | [![GitHub Actions](https://github.com/cordada/lib-pe-sunat-python/actions/workflows/ci-cd.yaml/badge.svg?branch=develop)](https://github.com/cordada/lib-pe-sunat-python/actions/workflows/ci-cd.yaml?query=branch:develop) |
| `master` | Production | [GitHub](https://github.com/cordada/lib-pe-sunat-python/tree/master) | [![GitHub Actions](https://github.com/cordada/lib-pe-sunat-python/actions/workflows/ci-cd.yaml/badge.svg?branch=master)](https://github.com/cordada/lib-pe-sunat-python/actions/workflows/ci-cd.yaml?query=branch:master) |


| Code Climate | Project Analysis |
| ------------ | ---------------- |
| [![Maintainability](https://api.codeclimate.com/v1/badges/ede6619f0d7dc4a0f0bc/maintainability)](https://codeclimate.com/github/cordada/lib-pe-sunat-python/maintainability) | [Open Source Insights](https://deps.dev/pypi/pe-sunat) |


| Code Coverage |
| ------------- |
| [![Codecov](https://codecov.io/gh/cordada/lib-pe-sunat-python/branch/develop/graph/badge.svg?token=T4NJV2PI6X)](https://codecov.io/gh/cordada/lib-pe-sunat-python) |


### Hosting

| Deployment Environment | Python Package Registry |
| ---------------------- | ----------------------- |
| Production | [PyPI](https://pypi.org/project/pe-sunat/) |


## Installation

Install Python package:

```sh
pip install pe-sunat
```


## Usage

```python
from cordada.pe_sunat.ruc.entities import Ruc


example_valid_ruc = Ruc('20131312955')
print(example_valid_ruc.digits, example_valid_ruc.check_digit)

example_invalid_ruc = Ruc('20131312950', validate_check_digit=True)
```


## Additional Documentation

[Documentation](docs/)
