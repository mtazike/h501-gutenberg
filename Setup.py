from setuptools import setup, find_packages

setup(
    name="tt_gutenberg",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
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