from setuptools import setup,find_packages

VERSION = '1.0.1'
DESCRIPTION = 'Find Github user basic details'
LONG_DESCRIPTION = "A simple python package that allows users to view a Github user's basic details"

# Setting up
setup(
    name="githubuser",
    version=VERSION,
    url='https://github.com/pranavvp10/githubuser',
    author="Pranav V P",
    author_email="<pranavvp07@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[ 'requests',],

    keywords=['python', 'Github', 'githubuser'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        'License :: OSI Approved :: MIT License',
        "Operating System :: Microsoft :: Windows",
    ]
)