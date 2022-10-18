import cv2
from typing import TypedDict
import os


class Template(TypedDict):
    name: str
    image: str


dirPath = os.path.dirname(os.path.abspath(__file__))

buy_button_covenant: Template = {
    "image": cv2.imread(dirPath + '/images/Buy_button_Covenant.png', 0),
    "name": "buy_button_covenant"
}
buy_button_mystic: Template = {
    "image": cv2.imread(dirPath + '/images/Buy_button_Mystic.png', 0),
    "name": "buy_button_mystic"
}
confirm_button: Template = {
    "image": cv2.imread(dirPath + '/images/confirm_button.png', 0),
    "name": "confirm_button"
}
covenant: Template = {
    "image": cv2.imread(dirPath + '/images/covenant.png', 0),
    "name": "covenant"
}
mystic: Template = {
    "image": cv2.imread(dirPath + '/images/mystic.png', 0),
    "name": "mystic"
}
refresh_button: Template = {
    "image": cv2.imread(dirPath + '/images/refresh_button.png', 0),
    "name": "refresh_button"
}

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

hunt_try_again: Template = {
    "image": cv2.imread(dirPath + '/images/hunt/try_again.png', 0),
    "name": "hunt_try_again"
}

hunt_confirm: Template = {
    "image": cv2.imread(dirPath + '/images/hunt/confirm.png', 0),
    "name": "hunt_confirm"
}

hunt_insufficient_energy: Template = {
    "image": cv2.imread(dirPath + '/images/hunt/insufficient_energy.png', 0),
    "name": "hunt_insufficient_energy"
}
