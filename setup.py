from setuptools import setup  # , find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tokima',
    version='0.0.1',
    author="Kentaro Matsuzaki",
    author_email="kentaro0919@gmail.com",
    description='A Utility Tools',
    long_description=long_description,
    url="https://github.com/kentaro0919/tokima",
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.6',
                 ],
    )
