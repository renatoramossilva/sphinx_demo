# Sphinx demo

To verify them locally, [install Poetry](https://python-poetry.org/docs/) and execute the following in the root of this repository:

```shell
poetry install --no-root
poetry shell
make test
```

# Edit web page

- Edit *.py files adding/editing docstring.
- Creating a new py file, this config must be added in `docs/index.rst`.

```shell
make HTML
open _build/html/index.html
```

# Documentation

https://sphinx-demo-r2s.readthedocs.io/en/latest/index.html

