from setuptools import setup, find_packages

with open('README.rst') as f:
    README = f.read()

classifiers = ["Programming Language :: Python",
               "License :: OSI Approved :: Apache Software License",
               "Development Status :: 4 - Beta"]


setup(name='requests-eventsource',
      version='0.0.1',
      url='https://github.com/tOkeshu/requests-eventsource',
      packages=find_packages(),
      long_description=README,
      description="Requests + EventSource = <3",
      author="Romain Gauthier",
      author_email="romain.gauthier@monkeypatch.me",
      include_package_data=True,
      install_requires=['requests'],
      classifiers=classifiers)
