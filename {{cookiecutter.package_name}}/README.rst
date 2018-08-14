{{ cookiecutter.package_name }}
{{ '=' * cookiecutter.package_name|length }}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg
   :target: https://pypi.org/project/{{ cookiecutter.package_name }}/
   :alt: Latest Version

.. image:: https://codecov.io/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/{{ cookiecutter.package_name }}/badge/?version=latest
   :target: https://{{ cookiecutter.package_name }}.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}.svg?branch=master
   :target: https://travis-ci.org/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}


TODO: Explain what your library does in one or two sentences.


Features
--------

* TODO: Provide a list of the main features of your library


Requirements
------------

{{ cookiecutter.package_name }} supports Python 3 only and requires at least Django 1.11.


Prepare for development
-----------------------

A Python 3.6 interpreter is required in addition to pipenv.

.. code-block:: shell

    $ pipenv install --python 3.6 --dev
    $ pipenv shell
    $ pip install -e .


Now you're ready to run the tests:

.. code-block:: shell

    $ pipenv run py.test


Resources
---------

* `Documentation <https://{{ cookiecutter.package_name }}.readthedocs.io>`_
* `Bug Tracker <https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}/issues>`_
* `Code <https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}/>`_
