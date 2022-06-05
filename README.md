# Simon

Four colored buttons light up in a specific pattern. After displaying the pattern, the player must repeat the pattern by clicking the buttons in proper order. The pattern gets longer each time the player completes the pattern. If the player presses a wrong button, the game ends.

This is one of my "Weekend Game" projects.
A "Weekend Game" is a small game idea that I implement in a single weekend using latest Python and Kivy framework.
Goal is to keep my software design & development skills up to date.

# Using

## Setting Up
    git clone git@github.com:jnmbk/wg-simon.git
    cd wg-boilerplate
    pip install -e .

## Running
    python -m game.main

## Building for Android
    pip install buildozer cython
    buildozer android debug deploy run

![Tests](https://github.com/jnmbk/wg-simon/actions/workflows/tests.yml/badge.svg)
