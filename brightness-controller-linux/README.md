# Brightness Controller for Linux

## Dev Docs

### Installing Dependencies
You will need [poetry](https://python-poetry.org/docs/#installation). After navigating to this directory, run the following:

```
poetry install
```

It will install dependencies as defined in `pyproject.toml`.


### Building

```
poetry build
```

### Running Brightness Controller

```
poetry run python src/brightness_controller_linux/init.py
```

### Testing

```
poetry run pytest
```