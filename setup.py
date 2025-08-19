# Code generated for API Clients. DO NOT EDIT.

import os.path

from setuptools import find_packages, setup


def read_file(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()


setup(
    name="ngrok-api",
    version="0.17.0",
    description="ngrok HTTP API client library",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    author="Alan Shreve",
    author_email="alan@ngrok.com",
    packages=find_packages(exclude=["tests"]),
    package_data={"ngrok": ["py.typed"]},
    url="https://github.com/ngrok/ngrok-api-python",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.1,<3.0",
    ],
    extras_require={
        "tox": ["tox==3.23.0"],
        "doc": [
            "black==21.5b1",
            "isort==5.11.5",
            "click==8.0.4",
            "furo==2022.12.7",
            "sphinx==6.1.3",
            "sphinx-autodoc-typehints==1.12.0",
            "sphinx-readable-theme==1.3.0",
            # Pin separately for https://github.com/sphinx-doc/sphinx/issues/10291
            "Jinja2==3.0.3",
        ],
    },
)
