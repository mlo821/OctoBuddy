
# coding=utf-8
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import RPi.GPIO as GPIO

def button_callback(channel):
    print("Button was pushed!")

class OctoBuddyPlugin(octoprint.plugin.StartupPlugin):
        def on_after_startup(self):
                self._logger.info("OctoBuddy Alive Now!")


GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.add_event_detect(8, GPIO.RISING, callback=button_callback)

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = OctoBuddyPlugin()
