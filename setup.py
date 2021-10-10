from setuptools import setup, find_packages

setup(
    name='AndyTEstf1234123',
    version='0.4.11',
    author='J. Random Hacker',
    author_email='jrh@example.com',
    packages=["cmdgrafanaclient"],
    #scripts=[],
    license='LICENSE.txt',
    description='Useful towel-related stuff.',
    long_description=open('README').read(),
    package_dir={"cmdgrafanaclient": "src"},
    install_requires=[],
)