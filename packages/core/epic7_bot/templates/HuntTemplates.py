import cv2
from epic7_bot.templates.BaseTemplates import BaseTemplates
from epic7_bot.templates.Template import Template


class HuntTemplates(BaseTemplates):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.try_again: Template = {
            "image": cv2.imread(self.dirPath + '/../images/hunt/try_again.png', 0),
            "name": "try_again"
        }

        self.confirm: Template = {
            "image": cv2.imread(self.dirPath + '/../images/hunt/confirm.png', 0),
            "name": "confirm"
        }

        self.insufficient_energy: Template = {
            "image": cv2.imread(self.dirPath + '/../images/hunt/insufficient_energy.png', 0),
            "name": "insufficient_energy"
        }

        self.pet_auto_battle_active: Template = {
            "image": cv2.imread(self.dirPath + '/../images/hunt/pet_auto_battle_active.png', 0),
            "name": "pet_auto_battle_active"
        }

        self.repeat_battling_has_ended: Template = {
            "image": cv2.imread(self.dirPath + '/../images/hunt/repeat_battling_has_ended.png', 0),
            "name": "repeat_battling_has_ended"
        }
        self.stage_clear: Template = {
            "image": cv2.imread(self.dirPath + '/../images/hunt/stage_clear.png', 0),
            "name": "stage_clear"
        }