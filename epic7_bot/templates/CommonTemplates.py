import cv2
import os
from epic7_bot.templates.BaseTemplates import BaseTemplates
from epic7_bot.templates.Template import Template


class CommonTemplates(BaseTemplates):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.skip_button: Template = {
            "image": cv2.imread(self.dirPath + '/../images/skip_button.png', 0),
            "name": "skip_button"
        }

        self.connecting_problem: Template = {
            "image": cv2.imread(self.dirPath + '/../images/connecting.png', 0),
            "name": "connecting_problem"
        }

        self.there_was_a_connection_error: Template = {
            "image": cv2.imread(self.dirPath + '/../images/there_was_a_connection_error.png', 0),
            "name": "there_was_a_connection_error"
        }
