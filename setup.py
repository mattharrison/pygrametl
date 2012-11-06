try:
    from setuptools import setup
except Exception as e:
    from distutils.core import setup

setup(name='pygrametl',
      version="0.2.0.2",
      packages=['pygrametl']
      )
