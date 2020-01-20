from setuptools import setup, find_packages
import sys, os

version = '0.6'

long_description = (
    open("README.rst").read()
    + '\n' +
    'Changes\n'
    '=======\n'
    + '\n' +
    open("docs/CHANGES.txt").read()
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    open("docs/CONTRIBUTORS.rst").read()
    + '\n')

setup(name='opencore-fassembler_projects',
      version=version,
      description="Assorted fassembler projects for creating repeatable OpenCore builds",
      long_description=long_description,
      # Get strings from https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Desktop Environment :: File Managers",
        "Topic :: Software Development :: Assemblers",
        "Topic :: System :: Systems Administration",
      ],
      keywords='fassembler projects frontend zine socialplanning opencore',
      author='Ethan Jucovy',
      author_email='opencore-dev@lists.coactivate.org',
      url='http://coactivate.org/projects/opencore',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "fassembler"
      ],
      ## FIXME: release all of these once fassembler stabilizes:
      dependency_links=[
          'https://github.com/socialplanning/fassembler/archive/master.zip#egg=fassembler',
      ],
      entry_points="""
      [fassembler.project]
      frontend = fassembler_projects.frontend:FrontendProject
      zine = fassembler_projects.zine:ZineProject
      """,
      )
