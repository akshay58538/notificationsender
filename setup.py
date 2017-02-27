import os
from codecs import open

from setuptools import setup, find_packages

ENV = os.environ.get('DEPLOYMENT_ENV') or 'dev'

package_name = 'notificationsender' + '-' + ENV

# Get the long description from the README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('VERSION', encoding='utf-8') as f:
    package_version = f.read()

dependencies = [
    'Flask==0.12',
    'Flask-SQLAlchemy==2.1',
    'Flask-Inputs==0.2.0',
    'jsonschema==2.6.0',
    'gunicorn',
    'enum34'
]

test_dependencies = [
    'nose==1.3.7',
    'mock==2.0.0'
]

print "**************************************************"
print "Installing package: " + package_name + " version: " + package_version
print "**************************************************"

setup(
    name=package_name,

    namespace_packages=['healthifyme'],

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=package_version,

    description='Project for sending notifications to users',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/akshay58538/notificationsender',

    # Author details
    author='Akshay Goel',
    author_email='akshay58538@gmail.com',

    # What does your project relate to?
    keywords='',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'scripts', 'build', 'dist']),
    package_data={
        'plivo': ['sms/config/*.json'],
        '': ['VERSION']
    },

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=dependencies,

    tests_require=test_dependencies,

    test_suite="tests",

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': ['coverage']
    }
)