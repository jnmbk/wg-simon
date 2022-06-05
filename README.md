# Weekend Game Boilerplate

This is a boilerplate for my future "Weekend Game" projects.
A "Weekend Game" is a small game idea that I implement in a single weekend using latest Python and Kivy framework.
Goal is to keep my software design & development skills up to date.

# Features of this boilerplate

* Uses pytest for testing
* Uses mypy for checking type hints
* Uses flake8 for linting and checking code style
* Uses tox for testing in multiple environments
* Uses GitHub actions for testing every push

# Using

## Setting Up
    git clone git@github.com:jnmbk/wg-boilerplate.git
    cd wg-boilerplate
    pip install -e .

## Running
    python -m game.main

## Building for Android
    pip install buildozer cython
    buildozer android debug deploy run

![Tests](https://github.com/jnmbk/wg-boilerplate/actions/workflows/tests.yml/badge.svg)
