from setuptools import setup
import os

with open(os.path.join(os.getcwd(), 'VERSION')) as version_file:
    version = version_file.read().strip()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="Kit Plummer",
    author_email="kitplummer@gmail.com",
    name="clikan",
    url="https://github.com/kitplummer/clikan",
    version=version,
    description="Simple CLI-based Kanban board",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['clikan'],
    install_requires=[
        'Click',
        'click-default-group',
        'pyyaml',
        'rich'
    ],
    entry_points='''
        [console_scripts]
        clikan=clikan:clikan
    ''',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Environment :: Console"
    ]
)
