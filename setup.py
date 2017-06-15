import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_layout',
    ]


setup(name='pyramid_flash_message',
      version='0.2.2',
      description='Small tool to add and show flash messages',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Sayyid Hamid Mahdavi',
      author_email='sayyid.hamid.mahdavi@gmail.com',
      url='https://github.com/sahama/pyramid_flash_message',
      keywords='web wsgi bfg pylons pyramid flash message',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={},
      install_requires=requires,
      )
