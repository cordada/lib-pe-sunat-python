# Development

## Tools

This project uses the following development tools:

- [Flake8](https://flake8.pycqa.org/): Python static code analyzer (or *linter*).
- [Mypy](http://www.mypy-lang.org/): Static type checker for Python.
- [Isort](https://pycqa.github.io/isort/): Python utility to sort imports alphabetically, and
  automatically separated into sections and by type.
- [Black](https://github.com/psf/black/): Python code formatter.


## Building

Run the following command:

```sh
make build

make dist
```


## Linting

Run the following command:

```sh
make lint
```

Some lint errors can be automatically fixed by running the following command:

```sh
make lint-fix
```


## Testing

```sh
make test
```


## Adding Python Dependencies

- Add package to `requirements.in` (base & production environments) or `requirements-dev.in`
  (development, testing, and release environments).
- Run `make python-deps-compile`.
- Run `git add requirements.txt requirements-dev.txt`.
