# coding=utf-8
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import RPi.GPIO as GPIO


import os

bouncetime_button = 400

class OctoBuddyPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.ShutdownPlugin):

    def on_after_startup(self):
        self._logger.info("OctoBuddy Alive Now!")
        self._logger.info(self._printer.get_state_id())
        self._logger.info(GPIO.RPI_INFO)
        self.setup_GPIO();

    def on_shutdown(self):
        GPIO.cleanup();
        self._logger.info("OctoBuddy Going to Bed Now!")
        self._logger.info("Test")

    def button_callback(self, channel):
        self._logger.info("test")
        self._logger.info("and I have to type this again")

        if channel == 22:
            self._printer.home("x")
            self._printer.home("y")
            self._printer.home("z")

    def setup_GPIO(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(22, GPIO.RISING, callback=self.button_callback, bouncetime = bouncetime_button)
        GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(24, GPIO.RISING, callback=self.button_callback, bouncetime = bouncetime_button)




__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = OctoBuddyPlugin()
