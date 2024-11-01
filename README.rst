pymodaq_plugins_arduino_ubuntu
##############################

.. the following must be adapted to your developed package, links to pypi, github  description...

.. image:: https://img.shields.io/pypi/v/pymodaq_plugins_template.svg
   :target: https://pypi.org/project/pymodaq_plugins_template/
   :alt: Latest Version

.. image:: https://readthedocs.org/projects/pymodaq/badge/?version=latest
   :target: https://pymodaq.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://github.com/PyMoDAQ/pymodaq_plugins_template/workflows/Upload%20Python%20Package/badge.svg
   :target: https://github.com/PyMoDAQ/pymodaq_plugins_template
   :alt: Publication Status

.. image:: https://github.com/PyMoDAQ/pymodaq_plugins_template/actions/workflows/Test.yml/badge.svg
    :target: https://github.com/PyMoDAQ/pymodaq_plugins_template/actions/workflows/Test.yml

This plugin allows to read an analog output of an Arduino board with PyMoDAQ on Ubuntu.

Authors
=======

* David Bresteau (david.bresteau@cea.fr)

Instruments
===========

Below is the list of instruments included in this plugin

Viewer0D
++++++++

* **Arduino analog output**: reading of the analog output of an Arduino board.

Installation instructions
=========================

For complete instructions, go to exemples section at https://pymodaq.cnrs.fr/en/5.0.x_dev/index.html

* PyMoDAQ version 4.4.6
* Operating system: Xubuntu 22.04

Run the Arduino IDE with an AppImage (equivalent to a .exe file on Windows) for example:
https://appimage.github.io/Arduino_IDE/

The Pyfirmata2 server should be uploaded into the connected Arduino board with the Arduino IDE.
Instructions can be found here: https://pypi.org/project/pyFirmata2/#description or here
https://github.com/berndporr/pyFirmata2
