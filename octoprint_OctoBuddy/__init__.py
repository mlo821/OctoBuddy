
# coding=utf-8
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import RPi.GPIO as GPIO

class OctoBuddyPlugin(octoprint.plugin.StartupPlugin):
        def on_after_startup(self):
                self._logger.info("OctoBuddy Alive Now!")

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = OctoBuddyPlugin()
