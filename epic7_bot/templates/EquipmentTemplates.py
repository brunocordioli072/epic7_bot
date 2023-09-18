import cv2
from epic7_bot.templates.BaseTemplates import BaseTemplates
from epic7_bot.templates.Template import Template


class EquipmentTemplates(BaseTemplates):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.equipment_blue: Template = {
            "image": cv2.imread(self.dirPath + '/../images/equipment/Equipment_blue.png', 0),
            "name": "equipment_blue"
        }

