#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


def read_file(file_name):
    """Read file and return its contents."""
    with open(file_name, "r", encoding="utf8") as f:
        return f.read()


def read_requirements(file_name):
    """Read requirements file as a list."""
    reqs = read_file(file_name).splitlines()
    return reqs


setup(
    name="plairghgt",
    version="1.0.0",
    author="UI Test",
    description="UI Test",
    keywords=[],
    classifiers=[],
    package_dir={"": "."},
    packages=find_packages(where="."),
    package_data={
        "data": ["resources/*"],
    },
    install_requires=read_requirements("requirements.txt"),
    python_requires=">=3.13.0",
    license="MIT",
)