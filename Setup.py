from setuptools import setup, find_packages

setup(
    name="tt_gutenberg",
    version="0.1.0",
    author="Mahya Tazike",
    author_email="mtazike@iu.edu",
    description="A package for working with Project Gutenberg author data",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)