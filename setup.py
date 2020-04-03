#!/usr/bin/env python
# pylint: disable=missing-docstring
from setuptools import setup


with open('README.rst') as readme:
    LONG_DESCRIPTION = readme.read()


REQUIREMENTS = open('requirements.txt').readlines()


setup(name='kiwitcms-junit.xml-plugin',
      version='8.2',
      packages=['tcms_junit_plugin'],
      scripts=['tcms-junit.xml-plugin'],
      description='junit.xml plugin for '
                  'Kiwi TCMS test case management system',
      long_description=LONG_DESCRIPTION,
      author='Kiwi TCMS',
      author_email='info@kiwitcms.org',
      license='GPLv3+',
      url='https://github.com/kiwitcms/junit.xml-plugin',
      install_requires=REQUIREMENTS,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v3 '
          'or later (GPLv3+)',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
      ])
