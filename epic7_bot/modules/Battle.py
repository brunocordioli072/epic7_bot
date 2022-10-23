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

    def do_rotation(self):
        try_again_button, confirm_button = None, None

        logging.debug(
            f"Wait for try again button or confirm button to appear")
        while try_again_button is None and confirm_button is None:
            try_again_button, confirm_button = self.check_try_again_and_confirm_buttons()
            time.sleep(1)

        if confirm_button is not None:
            self.ScreenManager.click_middle_and_check_change_on_area_retry(
                x1=1395, y1=808, x2=1492, y2=839, action="Click on confirm button")

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=1416, x2=1533, y1=810, y2=841, action="Click on try again button")

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=1404, y1=811, x2=1469, y2=842, action="Click on start button")

        if self.ScreenManager.match_template_on_screen_area(
                x1=629, y1=175, x2=960, y2=224, template=self.HuntTemplates.insufficient_energy, percentage=0.6) is not None:
            logging.debug(f"Insufficient Energy, finishing hunting")
            return

        self.do_rotation()

    def start_hunt(self):
        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=1404, y1=811, x2=1469, y2=842, action="Click on start button")

        self.do_rotation()
