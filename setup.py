
from setuptools import setup, find_packages


version = '0.1'
url = 'https://github.com/pmaigutyak/mp-static'

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name='django-mp-static',
    version=version,
    description='Django static app',
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url=url,
    download_url='{}/archive/{}.tar.gz'.format(url, version),
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    install_requires=requires
)
