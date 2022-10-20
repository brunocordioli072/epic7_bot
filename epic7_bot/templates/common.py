import cv2
import os
from epic7_bot.templates.base import Template


dirPath = os.path.dirname(os.path.abspath(__file__))

skip_button: Template = {
    "image": cv2.imread(dirPath + '/images/skip_button.png', 0),
    "name": "skip_button"
}

connecting_problem: Template = {
    "image": cv2.imread(dirPath + '/images/connecting.png', 0),
    "name": "connecting_problem"
}

there_was_a_connection_error: Template = {
    "image": cv2.imread(dirPath + '/images/there_was_a_connection_error.png', 0),
    "name": "there_was_a_connection_error"
}
