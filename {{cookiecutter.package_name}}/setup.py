import os
from codecs import open

from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('{{ cookiecutter.module_name }}').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='{{ cookiecutter.package_name }}',
    version=VERSION,
    description='TODO: Explain what your libraries does.',
    long_description=long_description,
    url='https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}',
    project_urls={
        'Bug Reports': 'https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}/issues',
        'Source': 'https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}',
    },
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[],
    include_package_data=True,
    keywords='django',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
