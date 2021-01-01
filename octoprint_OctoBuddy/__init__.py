# coding=utf-8
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import RPi.GPIO as GPIO


import os

bouncetime_button = 400

class OctoBuddyPlugin(octoprint.plugin.StartupPlugin,
					  octoprint.plugin.ShutdownPlugin,
					  octoprint.plugin.SettingsPlugin,
					  octoprint.plugin.TemplatePlugin):

    def on_after_startup(self):
        self._logger.info("OctoBuddy Alive Now!")
    #    self._logger.info(self._printer.get_state_id())
    #    self._logger.info(GPIO.RPI_INFO)
    #    self.setup_GPIO()

    #def on_shutdown(self):
    #    GPIO.cleanup()
    #    self._logger.info("OctoBuddy Going to Bed Now!")

    #def button_callback(self, channel):
    #    self._logger.info(channel + "Pressed")

    #    if channel == home_pin:
    #        self._printer.home("x")
    #        self._printer.home("y")
    #        self._printer.home("z")

    #def setup_GPIO(self):
    #    GPIO.setwarnings(False)
    #    GPIO.setmode(GPIO.BOARD)
    #    GPIO.setup(self.home_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #    GPIO.add_event_detect(self.home_pin, GPIO.RISING, callback=self.button_callback, bouncetime = self.debounce)

    def get_settings_defaults(self):
        return dict(
			home_pin	= 23,   # Default is no pin
			debounce    = 400,  # Debounce
		)

    def get_template_configs(self):
        return [dict(type = "settings", custom_bindings=False)]
        self._logger.info("Setup Settings")

    #@property
    #def debounce(self):
    #    return int(self._settings.get(["debounce"]))

    #@property
    #def home_pin(self):
     #   return int(self._settings.get(["home_pin"]))

    def on_settings_save(self):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        self._logger.info("Settings Changed... maybe")
        #self._logger.info("OctoBuddy settings changed, updating GPIO setup")
        #self.setup_GPIO()
    
        
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = OctoBuddyPlugin()
