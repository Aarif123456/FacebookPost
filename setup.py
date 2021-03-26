import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FacebookPost", 
    version="0.0.1",
    author="Abdullah Arif",
    description="A bot to write to Facebook via selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aarif123456/FacebookPost",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)