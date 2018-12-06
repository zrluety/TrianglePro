from setuptools import setup, find_packages

install_requires = ['numpy']

setup(
    name='trianglepro',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    url='',
    license='',
    author='Zachary Luety',
    author_email='zluety@gpwa.com',
    description='An application for reserving'
)
