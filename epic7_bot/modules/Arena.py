import logging
import time
from epic7_bot.core.DeviceManager import DeviceManager
from epic7_bot.modules.Module import Module
from epic7_bot.templates.CommonTemplates import CommonTemplates


class Arena(Module):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.DeviceManager = DeviceManager()
        self.CommonTemplates = CommonTemplates()

    def battle_rotation(self):
        logging.info(f"Started battle rotation")

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1065, x2=1216, y1=799, y2=852, action="Click on start battle")

        time.sleep(4)

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1476, x2=1574, y1=23, y2=76, action="Click on skip")

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1379, x2=1439, y1=14, y2=68, action="Click on auto battle")

        logging.info(f"Wait for skip button to appear")
        while self.ScreenManager.match_template_on_screen_area(x1=1471, x2=1581, y1=19, y2=76,
                                                               template=self.CommonTemplates.skip_button, percentage=0.55) is None:
            time.sleep(1)

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1476, x2=1574, y1=23, y2=76, action="Click on skip button")

        time.sleep(2)

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1378, x2=1546, y1=802, y2=853, action="Click on confirm")

    def do_battle_rotation(self, x1, y1, x2, y2, action):
        clicked = self.ScreenManager.random_click_at_area_and_check_change_on_screen_retry(
            x1, y1, x2, y2, action, percentage=50)
        if clicked:
            self.battle_rotation()

    def scroll(self):
        self.DeviceManager.device.shell(
            "input touchscreen swipe 1200 700 1200 400 200")

    def scroll_and_do_battle_rotation(self, x1, y1, x2, y2, action):
        self.scroll()
        self.do_battle_rotation(x1, y1, x2, y2, action)

    def start_arena_npc_auto_battle(self):
        self.do_battle_rotation(x1=1109, x2=1212, y1=218, y2=294,
                                action="Click on first opponent")

        self.do_battle_rotation(x1=1115, x2=1208, y1=354, y2=418,
                                action="Click on second opponent")

        self.do_battle_rotation(x1=1117, x2=1203, y1=480, y2=544,
                                action="Click on third opponent")

        self.do_battle_rotation(x1=1117, x2=1207, y1=615, y2=681,
                                action="Click on fouth opponent")

        self.do_battle_rotation(x1=1114, x2=1212, y1=740, y2=815,
                                action="Click on fifth opponent")

        self.scroll_and_do_battle_rotation(x1=1121, x2=1209, y1=274, y2=339,
                                           action="Click on sixty opponent")

        self.scroll_and_do_battle_rotation(x1=1117, x2=1208, y1=408, y2=479,
                                           action="Click on seventy opponent")

        self.scroll_and_do_battle_rotation(x1=1117, x2=1203, y1=546, y2=594,
                                           action="Click on eighth opponent")

        self.scroll_and_do_battle_rotation(x1=1117, x2=1207, y1=676, y2=735,
                                           action="Click on nineth opponent")

        self.scroll_and_do_battle_rotation(x1=1114, x2=1212, y1=804, y2=865,
                                           action="Click on tenth opponent")

    def start_arena_npc_auto_battle_from_lobby(self):
        self.ScreenManager.ensure_not_on_sleep_mode_on_lobby()

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1022, x2=1129, y1=749, y2=882, action="Click on arena icon on lobby")

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=246, x2=438, y1=218, y2=283, action="Click on arena ranked")

        self.ScreenManager.random_click_at_area_and_check_change_on_area_retry(
            x1=1334, x2=1551, y1=236, y2=298, action="Click on NPC opponents")

        self.start_arena_npc_auto_battle()
