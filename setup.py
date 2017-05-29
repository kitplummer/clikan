from setuptools import setup

setup (
        name="clik",
        version='0.0.1',
        py_modules=['clik'],
        install_requires=[
            'Click',
            'pyyaml'
        ],
        entry_points='''
            [console_scripts]
            clik=clik:cli
        '''
)
