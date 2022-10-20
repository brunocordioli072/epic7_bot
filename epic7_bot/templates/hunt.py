import cv2
from epic7_bot.templates.base import Template
import os


dirPath = os.path.dirname(os.path.abspath(__file__))

try_again: Template = {
    "image": cv2.imread(dirPath + '/images/hunt/try_again.png', 0),
    "name": "try_again"
}

confirm: Template = {
    "image": cv2.imread(dirPath + '/images/hunt/confirm.png', 0),
    "name": "confirm"
}

insufficient_energy: Template = {
    "image": cv2.imread(dirPath + '/images/hunt/insufficient_energy.png', 0),
    "name": "insufficient_energy"
}
