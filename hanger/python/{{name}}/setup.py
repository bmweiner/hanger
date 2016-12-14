import sys
from setuptools import setup

exec(open('{{name}}/version.py').read())

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    with open('README.md') as file:
        long_description = file.read()

setup(name='{{name}}',
      version=__version__,
      author='{{author}}',
      author_email='{{email}}',
      url='{{github}}/{{name}}',
      description=__description__,
      long_description=long_description,
      license='{{license}}',
      classifiers = [
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
      platforms=['py27', 'py35'],
      packages=['{{name}}',
                '{{name}}.tests'],
      install_requires=[{{deps}}],
      setup_requires=[] + pytest_runner,
      tests_require=['pytest'])
