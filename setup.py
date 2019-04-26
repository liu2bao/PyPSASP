import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyPSASP",
    version="0.1.3",
    author="liu2bao",
    author_email="liu2bao@yeah.net",
    description="Use python to manipulate PSASP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liu2bao/PyPSASP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
)