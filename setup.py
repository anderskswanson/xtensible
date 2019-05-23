import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xtensible-bot",
    version="0.0.1",
    author="Anders Swanson",
    author_email="anders.swanson.93@gmail.com",
    description="A modular discord bot supporting static loading of APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anderskswanson/xtensible-bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
