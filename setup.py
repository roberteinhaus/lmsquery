import lmsquery.constants
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "LMSQuery",
    version = lmsquery.constants.LMSQUERY_VERSION,
    author = "Robert Einhaus",
    author_email = "robert@einhaus.info",
    description = ("Query library for Logitech Media Server"),
    license = "MIT",
    keywords = "logitech media server lms",
    url = "https://github.com/roberteinhaus/lmsquery",
    packages=['lmsquery'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
