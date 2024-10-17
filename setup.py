

from setuptools import setup, find_packages # type: ignore

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="package_name",
    version="0.0.1",
    author="Joao Guilherme",
    author_email="joaoguilhermegs00@gmail.com",
    description="image processing package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Joao-Guilherme88/Guinder",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)