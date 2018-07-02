"""Setup script for installing hugs."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'hugs',
    'author': 'John R. Leeman',
    'url': 'Project URL https://github.com/jrleeman/SettingUpOpenSource',
    'download_url': 'https://github.com/jrleeman/SettingUpOpenSource',
    'author_email': 'kd5wxb@gmail.com',
    'version': '0.1',
    'install_requires': ['numpy', 'matplotlib'],
    'packages': ['hugs'],
    'scripts': [],
    'name': 'hugs'
}

setup(**config)
