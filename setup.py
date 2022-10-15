
import setuptools

with open('reqs.txt') as f:
    required = f.read().splitlines()
    print(required)

setuptools.setup(
    name='requests_logger',
    version='0.0.0-dev',
    description='Log all Requests',
    author='Lama Jan',
    install_requires=required,
    packages=['requests_logger'],

)