from setuptools import setup, find_packages
from easy_tools import __version__ as version


setup(
    name='Django Easy Tools',
    version=version,
    description='A simple tools library for expedite yours projects.',
    author='Jesus Anaya',
    author_email='jesus.anaya.dev@gmail.com',
    license="BSD",
    include_package_data=True,
    url='https://github.com/JesusAnaya/django-easy-tools/',
    packages=find_packages(),
)
