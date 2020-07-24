===========
eox-essence
===========

.. image:: https://circleci.com/gh/eduNEXT/eox-essence.svg?style=shield
    :target: https://circleci.com/gh/eduNEXT/eox-essence

.. image:: https://codecov.io/gh/eduNEXT/eox-essence/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/eduNEXT/eox-essence

Usage
#####

Central interface between edx-platform dependencies and any other external plugin, by default it provides the ability to use platform dependencies, however it is possible to toggle this behavior in the settings section so that each dependency can be replaced with a similar one.

Settings
********
This values can be modified in the following enviroments:

Ironwood:
++++++++
lms.env.json and cms.env.json

Juniper:
++++++++
/edx/etc/lms.yml and /edx/etc/studio.yml

Mimic
********

In test environments the edx-platform absence makes too complex to run unit testing, this dependency provides alternative modules that allow testing isolated environments. The main purpose is to avoid ImportError exceptions, however if you intend to use a method or class attribute the best option is to use a mock in the corresponding test.

How to use
**********

First of all you have to verify, if the dependency exist in our list, then import it from the edxapp package.

Example:
++++++++

.. code-block:: python

  from eox_essence.edxapp.site_configuration import helpers

Supported Dependencies.
########
Dependencies list.
-

Installation
############

Open edX devstack
*****************

- Clone this repo in the src folder of your devstack.
- Open a new Lms/Devstack shell.
- Install the plugin as follows: pip install -e /path/to/your/src/folder
- Restart Lms/Studio services.

Contributing
############

Add your contribution policy. (If required)