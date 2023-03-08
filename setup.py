"""
Toolkit
-------

Assorted utilities from Algoshelf.
"""

from setuptools import setup, find_packages
from pathlib import Path

def get_version():
    """Returns the package version taken from version.py.
    """
    path = Path(__file__).parent / "toolkit" / "version.py"
    code = path.read_text()
    env = {}
    exec(code, env, env)
    return env['__version__']

__version__ = get_version()

install_requires = ['web.py', 'psycopg2-binary', 'pyYAML', 'click']
extras_require = {
    'all': ['requests'],
    'data': ['pandas']
}

setup(
    name='toolkit',
    version=__version__,
    author='Pipal Academy',
    author_email='hello@pipal.in',
    description='Assorted utilities from Pipal Academy',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points = {
        'console_scripts': ['validate-fileformat=toolkit.cli:validate_fileformat'],
    }
)
