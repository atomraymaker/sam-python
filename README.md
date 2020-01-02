# AWS SAM Python Cookiecutter

A cookie cutter template for AWS SAM.

Usage:

`sam init --location gh:atomraymaker/sam-python`

Includes:

- pytest
- pytest-cov
- pytest-pylint
- pytest-mypy
- pytest-black
- and more...

## Configuration

### iSort

Isort is enabled on save in vscode settings by:

```{json}
"editor.codeActionsOnSave": {
    "source.organizeImports": true,
}
```

Configuration is customized in isort.cfg to be consistent with black as per [these docs](https://black.readthedocs.io/en/stable/the_black_code_style.html) (search for isort)

## Venv

Using `PIPENV_VENV_IN_PROJECT=true` will create a .venv in the project folder. There is vscode config to reference the project python, black, pylint, and mypy rather than any global installs of these.

## pytest-pythonpath

Due to how SAM packages code, it can be difficult to get imports to work in unit tests and also when deployed. Referencing `CodeUri: app` causes SAM to package everythin in the app directory. It doesn't include the app directory, anything in there ends up at the top level when deployed. This means that `from app import module` does not work when deployed, but  `import module` doesn't work locally since it is nested in the app folder. Using `pytest-pythonpath` fixes this by moving everything in app to the top level, emulating the deployed state.

## Structlog

TODO
