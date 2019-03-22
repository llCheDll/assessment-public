from setuptools import setup
from setuptools import find_packages


setup(
    name="client",
    version="0.1",
    author="Archie Norman",
    author_email="archie@mercuryassets.io",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
)
