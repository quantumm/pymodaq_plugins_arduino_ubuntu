import numpy as np
import time

from pymodaq.utils.daq_utils import ThreadCommand
from pymodaq.utils.data import DataFromPlugins, DataToExport
from pymodaq.control_modules.viewer_utility_classes import DAQ_Viewer_base, comon_parameters, main
from pymodaq.utils.parameter import Parameter

from pyfirmata2 import Arduino

PORT = Arduino.AUTODETECT
## If AUTODETECT fails, enter the port name manually
## PORT = /ttyACM0
## You may have to change the access rights to the file that represents the port:
## sudo chmod a+rw /dev/ttyACM0
## This file seems to be created at every startup of the operating system. It could then be necessary to redo this
## operation each time one unplug/plug the board, or restart the computer.


class DAQ_0DViewer_ArduinoUbuntu(DAQ_Viewer_base):
    """ Instrument plugin class for a OD viewer.

    This object inherits all functionalities to communicate with PyMoDAQ’s DAQ_Viewer module through inheritance via
    DAQ_Viewer_base. It makes a bridge between the DAQ_Viewer module and the Python wrapper of a particular instrument.

    This plugin is made to read an analog output of an Arduino board with PyMoDAQ.

    Tested with an Arduino Uno, Arduino IDE 2.2.3
    Firmata Standard server
    Pyfirmata2 2.5.0
    Pymodaq 4.4.6
    Xubuntu 22.04

    The Firmata server should be uploaded into the connected Arduino board with the Arduino IDE.
    Instructions can be found here: https://pypi.org/project/pyFirmata2/#description or here
    https://github.com/berndporr/pyFirmata2

    Attributes:
    -----------
    controller: pyfirmata2.Arduino object
        Object that allow the communication with the board.
    """
    params = comon_parameters+[
        ]

    def ini_attributes(self):

        self.controller: Arduino = None

        self.samplingRate = 5  # sampling rate in Hz
        self.timestamp = 0

    def commit_settings(self, param: Parameter):
        """Apply the consequences of a change of value in the detector settings

        Parameters
        ----------
        param: Parameter
            A given parameter (within detector_settings) whose value has been changed by the user
        """

    def ini_detector(self, controller=None):
        """Detector communication initialization

        Parameters
        ----------
        controller: pyfirmata2.Arduino object
            custom object of a PyMoDAQ plugin (Slave case). None if only one actuator/detector by controller
            (Master case)

        Returns
        -------
        info: str
        initialized: bool
            False if initialization failed otherwise True
        """

        self.ini_detector_init(slave_controller=controller)

        if self.is_master:
            self.controller = Arduino(PORT)

        info = "Board initialized!"

        initialized = True
        return info, initialized

    def close(self):
        """Terminate the communication protocol"""
        ## TODO for your custom plugin
        raise NotImplemented  # when writing your own plugin remove this line
        #  self.controller.your_method_to_terminate_the_communication()  # when writing your own plugin replace this line

    def grab_data(self, Naverage=1, **kwargs):
        self.controller.analog[0].register_callback(self.callback)
        self.controller.samplingOn(1000 / self.samplingRate)
        self.controller.analog[0].enable_reporting()

    def callback(self, data):
        temperature = (data*5000 - 500)/10
        data_tot = temperature
        self.timestamp += (1 / self.samplingRate)
        self.dte_signal.emit(DataToExport(name='arduino_ubuntu_plugin',
                                          data=[DataFromPlugins(name='Mock1', data=data_tot,
                                                                dim='Data0D', labels=['dat0', 'data1'])]))

    def stop(self):
        """Stop the current grab hardware wise if necessary"""
        ## TODO for your custom plugin
        raise NotImplemented  # when writing your own plugin remove this line
        self.controller.your_method_to_stop_acquisition()  # when writing your own plugin replace this line
        self.emit_status(ThreadCommand('Update_Status', ['Some info you want to log']))
        ##############################
        return ''


if __name__ == '__main__':
    main(__file__)
