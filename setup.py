import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="sphinx_man",
    version="0.0.1",
    author="Paul Whipp <paul.whipp@gmail.com>",
    author_email="paul.whipp@gmail.com",
    description="Experiment into creating a protected repository that uses signatures and signing rules to allow pushes",
    url="git@github.com:pwhipp/sphinx_man.git",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"])
