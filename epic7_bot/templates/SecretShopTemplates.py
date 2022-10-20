import cv2
from epic7_bot.templates.BaseTemplates import BaseTemplates
from epic7_bot.templates.Template import Template


class SecretShopTemplates(BaseTemplates):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.buy_button_covenant: Template = {
            "image": cv2.imread(self.dirPath + '/../images/secret_shop/Buy_button_Covenant.png', 0),
            "name": "buy_button_covenant"
        }

        self.buy_button_mystic: Template = {
            "image": cv2.imread(self.dirPath + '/../images/secret_shop/Buy_button_Mystic.png', 0),
            "name": "buy_button_mystic"
        }

        self.covenant: Template = {
            "image": cv2.imread(self.dirPath + '/../images/secret_shop/covenant.png', 0),
            "name": "covenant"
        }

        self.mystic: Template = {
            "image": cv2.imread(self.dirPath + '/../images/secret_shop/mystic.png', 0),
            "name": "mystic"
        }
