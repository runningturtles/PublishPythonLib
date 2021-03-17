from setuptools import setup

setup(
    name='my first package',
    version='0.0.1',
    description='testing to build and publish python package from github repo',
    url='https://github.com/runningturtles/build_and_publish_python_package.git',
    author='Running Turtles',
    author_email='wangxn@gmx.com',
    license='unlicense',
    packages=['my_first_package'],
    zip_safe=False
)
