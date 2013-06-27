from setuptools import setup


if __name__ == '__main__':
  setup(
    name='Flask-Upstatic',
    description="Opinionated library for working with CDNs in Flask.",
    long_description=open('README.rst').read(),
    version='0.0.1',
    author='Mark Steve Samson',
    author_email='marksteve@insynchq.com',
    license='MIT',
    py_modules=['flask_upstatic'],
    install_requires=[
      'boto',
    ]
  )
