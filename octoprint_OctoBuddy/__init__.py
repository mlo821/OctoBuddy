
# coding=utf-8
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import RPi.GPIO as GPIO

buttonpressed = False
import os


class OctoBuddyPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.ShutdownPlugin):
    def on_after_startup(self):
        self._logger.info("OctoBuddy Alive Now!")
        self._logger.info(buttonpressed)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(11, GPIO.BOTH, callback=self.button_callback, bouncetime = 100)
        #GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self._logger.info(GPIO.RPI_INFO)
		self.testLogging("This is a message")
        #GPIO.add_event_detect(12, GPIO.BOTH, callback=button_callback, bouncetime = 100)
        #GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(13, GPIO.BOTH, callback=button_callback, bouncetime = 100)
        #GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(15, GPIO.BOTH, callback=button_callback, bouncetime = 100)
        #GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(16, GPIO.BOTH, callback=button_callback, bouncetime = 100)
        #GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(21, GPIO.BOTH, callback=button_callback, bouncetime = 100)
        #GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(22, GPIO.BOTH, callback=button_callback, bouncetime = 100)
        #GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(23, GPIO.BOTH, callback=button_callback, bouncetime = 100)
        #GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(24, GPIO.BOTH, callback=button_callback, bouncetime = 100)

    def on_shutdown(self):
        GPIO.cleanup();
        self._logger.info("OctoBuddy Going to Bed Now!")
        self._logger.info(buttonpressed)

    def button_callback(self, channel):
        self._logger.info("Button Pressed")

    def testLogging(message):
        self._logger.info(message)


__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = OctoBuddyPlugin()
