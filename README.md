# PE-SUNAT Python Library

This is a Python library for the *Superintendencia Nacional de Aduanas y de Administración
Tributaria* (SUNAT) of *Perú*.


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


## Development

[Development Documentation](docs/Development.md)
