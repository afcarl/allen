from io import open

from setuptools import find_packages, setup

with open('allen/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = ['numpy', 'scipy', 'pandas',
            'scikit-plot', 'scikit-learn', 'datacleaner']

setup(
    name='allen',
    version=version,
    description='',
    long_description=readme,
    author='bharath g.s',
    author_email='royalkingpin@gmail.com',
    maintainer='bharath g.s',
    maintainer_email='royalkingpin@gmail.com',
    url='https://github.com/_/allen',
    license='MIT/Apache-2.0',

    keywords=[
        'data assistant', 'allen', 'prediction'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
)
