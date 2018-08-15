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

## Work through TODOs

Now go an search for all TODOs inside the new generated project.

Most TODOs are documentation related. Please fill in some sane content.


## Docs

Please write some documentation for your library. In addition, you might genrate
some API documentation based on your docstrings.

```bash
	make apidoc
	make docs
```


## Enable CI on Travis

After you have pushed your first commits to GitHub, you might want to have your
tests run on every commit. Luckily, you get a CI for free if your package is
available publicly on GitHub.

To enable the CI, go to https://travis-ci.org/<github_user>/<package_name>,
for example https://travis-ci.org/stephrdev/django-tapeforms and make sure
you're logged in. 

If everythings worked you should see a message like "This is not an active
repository". Click on the "Activate repository" button.

Done.


## Enable documentation hosting with ReadTheDocs

Similar to Travis, ReadTheDocs provides documentation hosting for open source
projects. But think of giving some money to them if you or your company can effort it.

Now, to enable the documentation hosting, go to https://readthedocs.org/dashboard/
and click the "Import" button. On the next page, you should see your GitHub repository.
If not, click the "Import manually" button.

Provide the name (should be the same as on GitHub, your package name, for example
django-tapeforms) and enter the repository url on GitHub.

Some fine tuning is required to have everything right. Go to the "Admin" page and
change the Programming language to Python.

On the "Advanced settings" page, update the "Requirements file" field and insert
"docs/requirements.txt". Remember to also update the Python interpreter to 3.x.

To automatically trigger new builds upon every commit, go to the "Integrations"
page and open the "GitHub incoming webhook". On the next page, copy the webhook url -
something like "https://readthedocs.org/api/v2/webhook/<package_name>/123123/".

Take this url and go to the "Webhooks" section in your GitHub repository settings.
Click "Add webhook" and insert the RTD Webhook url as the payload url.
Complete the form by clicking "Add webhook".

Done.


## Publishing your package


To release and publish your package on PyPI, you should bump the version of your
package by updating the __version__ attribute of the __init__ module of your package.

You should try to stick to SemVer or CalVer for versioning.

In addition is it really important to maintain a changelog. To do so, this cookiecutter
template generates a CHANGELOG.rst (which is also included in the docs).

If both version and changelog are ready, use the make target "release" to put
your project to PyPI.

```bash
	make release
```
