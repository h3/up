from distutils.core import setup

try:
    import setuptools
except ImportError:
    pass

install_requires = [
    'PyYAML',
    'Yapsy',
]

setup(name='up',
      # Keep version in sync with up/__init__.py, Install section
      # of README.rst, and USER_AGENT in scripts/pypi-install.
      version=__import__('up').__version__,
      author='Maxime Haineault',
      author_email='max@haineault.com',
      description='Deployment experiment with fabric, yaml',
      long_description=open('README.rst').read(),
      license='GPLv2',
      url='http://github.com/h3/up',
      packages=['up'],
      scripts=['scripts/up', 'scripts/down'],
      install_requires=install_requires,
)
