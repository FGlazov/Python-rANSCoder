import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_rans",
    version="1.0.2",
    author="Fedor Glazov",
    author_email="fedorglazov@gmail.com",
    description="A lightweight, pure python implementation of a rANS coder.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ],
)