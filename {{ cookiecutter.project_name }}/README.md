# Workflow Engine

## Usage

### Install Dependencies

`PIPENV_VENV_IN_PROJECT=true pipenv sync --dev`

### Run Unit Tests

`pipenv run pytest`

## Configuration

### iSort

Isort is enabled on save in vscode settings by:

```
"editor.codeActionsOnSave": {
        "source.organizeImports": true,
    }
```

Configuration is customized in isort.cfg to be consistent with black as per [these docs](https://black.readthedocs.io/en/stable/the_black_code_style.html) (search for isort)

## Venv

Using `PIPENV_VENV_IN_PROJECT=true` will create a .venv in teh project folder. There is vscode config to reference the project python, black, pylint, and mypy rather than any global installs of these. 