import cv2
from epic7_bot.templates.base import Template
import os

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
