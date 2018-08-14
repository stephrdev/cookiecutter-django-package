# Cookiecutter Template for Django packages

This Cookiecutter template tries to help creating new Django packages which should
be installable via Pip / PyPI.


## Creation of the package

To start, use the Cookiecutter template to create the folder structure.

```bash
    cookiecutter /directory/to/cookiecutter-django-package
```


## First steps

After you created the package, some additional steps should be done:

```bash

    cd <repo_name>

    # Initialize git
    git init
    git remote add origin <remote git repository>

    # Setup Python environment
    pipenv install --python 3.6 --dev
    pipenv shell
    # Inside the created shell
    pip install -e .
    exit

    # Run tests for the first time
    make tests
```


## Docs

Please write some documentation for your library. In addition, you might genrate
some API documentation based on your docstrings.

```bash
	make apidoc
	make docs
```
