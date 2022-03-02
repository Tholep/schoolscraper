import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

requires = [
    'pip==19.0.3', # update pip
    'pandas==0.23.4', # Read the Excel file and preprocess as a dataframe
    'numpy==1.15.4', # Dependency of pandas library, used also for preprocessing data efficiently
    'items==0.6.5',
    'scrapy==1.8.2'
]

# entrypoints = {
#         'console_scripts': [
#             'bida = BIDA.bida:main',
#             'initialize_new_factory = BIDA.scripts.initialize_new_factory:main'
#         ]
#     }

setup(
    name='realestate',
    version='1.0.0',
    description='schoolscraper',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python'
    ],
    author='Lan Yen Dao Nguyen' + '\n\n' + 'Le Phuoc Tho',
    author_email='',
    url='',
    keywords='',
    packages=find_packages(), 
    include_package_data=True,
    zip_safe=False,
    install_requires=requires
)
