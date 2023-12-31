from setuptools import setup, find_packages

with open("/Users/fahadpatel/Downloads/orientation_detection/requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="orientationcheck",
    version="0.0.3",
    author="Nabila Lasri",
    author_email="lasri.nabilait@gmail.com",
    description=("This repository contains a Python program designed to execute Optical Character Recognition (OCR)"
                 " and Facial Recognition on images."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=required,
    include_package_data=True,
)
