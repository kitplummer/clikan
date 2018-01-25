from setuptools import setup

setup (
        author="Kit Plummer",
        author_email="kitplummer@gmail.com",
        name="clikan",
        version='0.0.1',
        py_modules=['clikan'],
        install_requires=[
            'Click',
            'pyyaml',
            'terminaltables'
        ],
        entry_points='''
            [console_scripts]
            clikan=clikan:cli
        ''',
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Environment :: Console"
        ]
)
