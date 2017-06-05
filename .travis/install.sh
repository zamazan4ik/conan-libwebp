#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update || brew update
    brew outdated pyenv || brew upgrade pyenv
    brew install pyenv-virtualenv

    if which pyenv > /dev/null; then
	eval "$(pyenv init -)"
    fi

    pyenv install $PYTHON_VERSION
    pyenv virtualenv $PYTHON_VERSION conan
    pyenv rehash
    pyenv activate conan
fi

pip install conan_package_tools # It install conan too
conan user
