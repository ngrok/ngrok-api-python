from setuptools import setup, find_packages
import os.path

def read_file(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()

setup(
    name="ngrok-api",
    version="0.1.2",
    description="ngrok HTTP API client library",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    author="Alan Shreve",
    author_email="alan@ngrok.com",
    packages=find_packages(exclude=['tests']),
    package_data={"ngrok": ["py.typed"]},
    url="https://github.com/ngrok/ngrok-api-python",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests==2.25.1",
    ],
    extras_require={
        "tox": ["tox==3.23.0"],
        "doc": ["black==21.5b1", "furo==2021.4.11b34", "sphinx==3.5.4", "sphinx-autodoc-typehints==1.12.0", "sphinx-readable-theme==1.3.0"],
    }
)
