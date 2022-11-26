#!/usr/bin/env bash

# runs pycodestyle against all python files in all folders

find . -type f -name "*.py" | xargs pycodestyle
