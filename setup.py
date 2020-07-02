import setuptools
import site
import sys

site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="idse",
    version="0.1.0",
    author="Kris",
    author_email="31852063+krisfris@users.noreply.github.com",
    description="Interactive data structure editing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krisfris/idse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'Click',
        'pyqt5',
    ],
    entry_points='''
        [console_scripts]
        idse=idse.cli:cli
    ''',
)
