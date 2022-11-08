import logging
import time
from epic7_bot.modules.Module import Module
from epic7_bot.templates.HuntTemplates import HuntTemplates


class Battle(Module):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.HuntTemplates = HuntTemplates()
        self.total_rotations = 0

    def has_energy(self):
        if self.ScreenManager.match_template_on_screen_area(
                x1=629, y1=175, x2=960, y2=224, template=self.HuntTemplates.insufficient_energy, percentage=0.6) is not None:
            logging.info(f"Insufficient Energy, finishing hunting")
            return False
        return True

    def do_hunt_rotation(self):
        self.show_stats()

        if self.has_energy() == False:
            return

        logging.info(
            f"Wait for repeat battling has ended to appear")
        while self.ScreenManager.match_template_on_screen(template=self.HuntTemplates.repeat_battling_has_ended, percentage=0.9) is None:
            time.sleep(1)

        self.total_rotations += 1

        if self.ScreenManager.match_template_on_screen_area(
                x1=1395, y1=808, x2=1492, y2=839, template=self.HuntTemplates.confirm, percentage=0.6) is not None:
            self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
                x1=1395, y1=808, x2=1492, y2=839, action="Click on confirm button")

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1416, x2=1533, y1=810, y2=841, action="Click on try again button")

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1404, y1=811, x2=1469, y2=842, action="Click on start button")

        if self.has_energy() == False:
            return

        self.do_hunt_rotation()

    def show_stats(self):
        comment = f"\nTotal Rotations: {str(self.total_rotations)}{' '*30} \n" \
            + f"{' '*30} \n"
        previus_line = "\033[F"
        if self.total_rotations == 0:
            print(f"\r{previus_line*2}{comment}")
        else:
            print(f"\r{previus_line*4}{comment}")

    def start_hunt(self):
        if self.ScreenManager.match_template_on_screen(template=self.HuntTemplates.pet_auto_battle_active, percentage=0.9) is None:
            self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
                x1=705, y1=675, x2=749, y2=718, action="Click on Pet Auto Battle Active", percentage=20)

        self.ScreenManager.random_click_at_area_and_check_change_on_screen_retry(
            x1=1404, y1=811, x2=1469, y2=842, action="Click on start button")

        self.do_hunt_rotation()

    def start_hunt_from_lobby(self):
        self.ScreenManager.ensure_not_on_sleep_mode_on_lobby()

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1164, y1=803, x2=1254, y2=870, action="Click on Battle button")

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=907, y1=648, x2=1055, y2=715, action="Click on Hunt button")

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=984, y1=259, x2=1113, y2=336, action="Click on Wyvern Hunt")

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1404, y1=810, x2=1559, y2=848, action="Click on Select Team")

        self.start_hunt()
