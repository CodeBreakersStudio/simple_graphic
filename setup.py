from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='simple_graphic',
    version='2020.2.23.1',
    #py_modules=['graphics'],
    packages=find_namespace_packages(include=['simple_graphic.*']) + ["simple_graphic"],
    description = "Simple to use graphic lib based on jminz work: https://github.com/jminz/graphics.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Kacper Kotlewski',
    #author_email='none',
    python_requires='>=3.7',
    install_requires=[
       "tkinter",
    ],
    url="https://github.com/KacperKotlewski/simple_graphic",
   )