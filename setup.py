from setuptools import setup

setup (
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
        '''
)
