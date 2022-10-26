import logging
import time
from epic7_bot.modules.Module import Module
from epic7_bot.templates.HuntTemplates import HuntTemplates


class Battle(Module):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.HuntTemplates = HuntTemplates()

    def check_try_again_and_confirm_buttons(self):
        try_again_button = self.ScreenManager.match_template_on_screen_area(
            x1=1416, x2=1533, y1=810, y2=841, template=self.HuntTemplates.try_again, percentage=0.6)
        confirm_button = self.ScreenManager.match_template_on_screen_area(
            x1=1395, y1=808, x2=1492, y2=839, template=self.HuntTemplates.confirm, percentage=0.6)
        return try_again_button, confirm_button

    def has_energy(self):
        if self.ScreenManager.match_template_on_screen_area(
                x1=629, y1=175, x2=960, y2=224, template=self.HuntTemplates.insufficient_energy, percentage=0.6) is not None:
            logging.debug(f"Insufficient Energy, finishing hunting")
            return False
        return True

    def do_hunt_rotation(self):
        try_again_button, confirm_button = None, None

        if self.has_energy() == False:
            return

        logging.debug(
            f"Wait for try again button or confirm button to appear")
        while try_again_button is None and confirm_button is None:
            try_again_button, confirm_button = self.check_try_again_and_confirm_buttons()
            time.sleep(1)

        time.sleep(6)

        if confirm_button is not None:
            self.ScreenManager.click_middle_and_check_change_on_area_retry(
                x1=1395, y1=808, x2=1492, y2=839, action="Click on confirm button")

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=1416, x2=1533, y1=810, y2=841, action="Click on try again button")

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=1404, y1=811, x2=1469, y2=842, action="Click on start button")

        if self.has_energy() == False:
            return

        self.do_hunt_rotation()

    def start_hunt(self):

        if self.ScreenManager.match_template_on_screen_area(
                x1=705, y1=675, x2=749, y2=718, template=self.HuntTemplates.pet_auto_battle_active, percentage=0.6) is None:
            self.ScreenManager.click_middle_and_check_change_on_area_retry(
                x1=705, y1=675, x2=749, y2=718, action="Click on Pet Auto Battle Active", percentage=20)

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=1404, y1=811, x2=1469, y2=842, action="Click on start button")

        self.do_hunt_rotation()

    def start_hunt_from_lobby(self):
        self.ScreenManager.ensure_not_on_sleep_mode_on_lobby()

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=1164, y1=803, x2=1254, y2=870, action="Click on Battle button")

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=907, y1=648, x2=1055, y2=715, action="Click on Hunt button")

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=984, y1=259, x2=1113, y2=336, action="Click on Wyvern Hunt")

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=1404, y1=810, x2=1559, y2=848, action="Click on Select Team")

        self.start_hunt()
