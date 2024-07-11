# setup.py

from setuptools import setup, find_packages

setup(
    name="software",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "software=main:main",
        ],
    },
)
