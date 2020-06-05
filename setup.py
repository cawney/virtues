try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': '13 Virtues',
        'author': 'James Carney',
        'url': 'URL to come',
        'download_url': 'URL to come',
        'author_email': 'my email',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': 'NAME',
        'scripts': [],
        'name': 'virtues'
        }

setup(**config)
