
# coding=utf-8
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import RPi.GPIO as GPIO

buttonpressed = False

def button_callback(channel):
    print("Button was pushed!")
    buttonpressed = True;

class OctoBuddyPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.ShutdownPlugin):
    def on_after_startup(self):
	    self._logger.info("OctoBuddy Alive Now!")
        self._logger.info(buttonpressed)

    def on_shutdown(self):
        GPIO.cleanup();
        self._logger.info("OctoBuddy Going to Bed Now!")
        self._logger.info(buttonpressed)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(11, GPIO.RISING, callback=button_callback, bouncetime = 200)

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = OctoBuddyPlugin()
