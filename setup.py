from setuptools import setup, find_packages

setup(
    name="ngrok-api-client",
    version="1.0.0",
    description="client Library for ngrok's HTTP API",
    author="Alan Shreve",
    author_email="alan@ngrok.com",
    packages=find_packages('ngrok'),
    package_data={"ngrok": ["py.typed"]},
    include_package_data=True,
    install_requires=[
        "requests==2.25.1",
    ],
    extras_require={
        "tox": ["tox==3.23.0"],
    }
)
