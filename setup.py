import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_rans",
    version="1.0.0",
    author="Fedor Glazov",
    author_email="fedorglazov@gmail.com",
    description="A lightweight, pure python implementation of a rANS coder.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Creative Commons Zero v1.0 Universal",
        "Operating System :: OS Independent",
    ],
)