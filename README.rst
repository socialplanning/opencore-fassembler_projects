============================
opencore-fassembler_projects
============================

Assorted fassembler projects for creating repeatable OpenCore builds. 
This package contains fassembler projects for building components of 
an `OpenCore <https://www.coactivate.org/projects/opencore/>`_ stack.


Features
========

This package provides two fassembler projects for an OpenCore site
installation:

Install Frontend
    Install the libopencore frontend that proxies over http to opencore,
    tasktracker and wordpress, with a Deliverance theme applied to the
    tasktracker and wordpress responses.

Install Zine
    Install the projects' Zine instances.


Installation
============

For install the latest released for this package, execute the following command:

::

  $ pip-2.4 install opencore-fassembler_projects

For install this package from development branch, execute the following command:

::

  $ pip-2.4 install git+https://github.com/socialplanning/fassembler#egg=fassembler
  $ pip-2.4 install git+https://github.com/socialplanning/opencore-fassembler_projects#egg=opencore-fassembler_projects


User / Developer Resources
==========================

* `The Opencore Project <http://www.coactivate.org/projects/opencore>`_

* `#opencore <irc://irc.freenode.net/opencore>`_


License
=======

The project is licensed under the **GPLv2**, more details see ``docs/LICENSE.txt`` file.
