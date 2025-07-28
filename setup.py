from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name="Celebrity Detection and QA",
    version="1.0.0",
    author="Oluchi",
    packages=find_packages(),
    install_requires=requirements,
)
