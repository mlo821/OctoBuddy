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
        self._logger.info(self._printer.get_state_id())
        self._logger.info(GPIO.RPI_INFO)
        self.setup_GPIO()



    def button_callback(self, channel):
        self._logger.info("%s was pressed, its state is %s = ", channel, GPIO.gpio_function(channel))

        if channel == self.home_pin:
            self._printer.home("x")
            self._printer.home("y")
            self._printer.home("z")

    def setup_GPIO(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        self.SetupSingleGPIO(self.home_pin)
        self.SetupSingleGPIO(self.resume_pin)
        self.SetupSingleGPIO(self.pause_pin)
        self.SetupSingleGPIO(self.x_pin_pos)
        self.SetupSingleGPIO(self.x_pin_neg)
        self.SetupSingleGPIO(self.y_pin_pos)
        self.SetupSingleGPIO(self.y_pin_neg)
        self.SetupSingleGPIO(self.z_pin_pos)
        self.SetupSingleGPIO(self.z_pin_neg)
        self.SetupSingleGPIO(self.e_stop_pin)
		#1
    def get_settings_defaults(self): 
        return dict(
		    home_pin	= 35,   
		    x_pin_pos   = 23,
		    x_pin_neg   = 29,
		    y_pin_pos   = 19,
		    y_pin_neg   = 21,
		    z_pin_pos   = 31,
		    z_pin_neg   = 33,
		    resume_pin  = 37,
		    pause_pin   = 15,
			e_stop_pin = -1,
			debounce    = 400,
			#2
		)

    def get_template_configs(self):
        return [dict(type = "settings", custom_bindings=False)]



    def on_settings_save(self, data):
        self.RemoveEventDetects(); #remove all active event detects
        GPIO.cleanup()
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        self._logger.info("OctoBuddy settings changed, updating GPIO setup")

        self.setup_GPIO()

    def SetupSingleGPIO(self, channel):
        try:
            if channel != -1:
 
                GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                GPIO.add_event_detect(channel, GPIO.RISING, callback=self.button_callback, bouncetime = self.debounce)
                self._logger.info("New Event Detect has been added to GPIO # %s", channel)
                self._logger.info("The new GPIO # %s state is %s ", channel, GPIO.gpio_function(channel))


        except:
            self._logger.exception("Cannot setup GPIO ports %s, check to makes sure you don't have the same ports assigned to multiple actions", str(channel))

    def RemoveEventDetects(self): #4
        try:
            GPIO.remove_event_detect(self.home_pin)
            GPIO.remove_event_detect(self.resume_pin)
            GPIO.remove_event_detect(self.pause_pin)
            GPIO.remove_event_detect(self.x_pin_pos)
            GPIO.remove_event_detect(self.x_pin_neg)
            GPIO.remove_event_detect(self.y_pin_pos)
            GPIO.remove_event_detect(self.y_pin_neg)
            GPIO.remove_event_detect(self.z_pin_pos)
            GPIO.remove_event_detect(self.z_pin_neg)
        except:
            self__logger.info("Issue with removing event detects.  Contact plugin owner")

    def on_shutdown(self):
        GPIO.cleanup()
        self._logger.info("OctoBuddy Going to Bed Now!")

    @property
    def debounce(self):
        return int(self._settings.get(["debounce"]))

    @property
    def home_pin(self):
        return int(self._settings.get(["home_pin"]))

    @property
    def pause_pin(self):
        return int(self._settings.get(["pause_pin"]))

    @property
    def resume_pin(self):
        return int(self._settings.get(["resume_pin"]))

    @property
    def x_pin_pos(self):
        return int(self._settings.get(["x_pin_pos"]))

    @property
    def x_pin_neg(self):
        return int(self._settings.get(["x_pin_neg"]))

    @property
    def y_pin_pos(self):
        return int(self._settings.get(["y_pin_pos"]))

    @property
    def y_pin_neg(self):
        return int(self._settings.get(["y_pin_neg"]))

    @property
    def z_pin_pos(self):
        return int(self._settings.get(["z_pin_pos"]))

    @property
    def z_pin_neg(self):
        return int(self._settings.get(["z_pin_neg"]))

    @property
    def e_stop_pin(self):
        return int(self._settings.get(["e_stop_pin"])) #3

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = OctoBuddyPlugin()
