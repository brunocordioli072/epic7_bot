import logging
import math
import asyncio
from epic7_bot.utils.runInParallel import runInParallel
from epic7_bot.core.DeviceManager import DeviceManager
from epic7_bot.core.MathUtils import MathUtils
from epic7_bot.modules.Module import Module
from epic7_bot.templates.EquipmentTemplates import EquipmentTemplates


class Equipment(Module):
    def __init__(self, fastMode):
        super(self.__class__, self).__init__()
        self.EquipmentTemplates = EquipmentTemplates()

    def craft_and_extract_blues(self):
        logging.info("Check Mystic and Covenant Bookmarks")

        [mystic_pos, coven_pos] = runInParallel(
            lambda: self.ScreenManager.match_template_on_screen(
                self.SecretShopTemplates.mystic),
            lambda: self.ScreenManager.match_template_on_screen(
                self.SecretShopTemplates.covenant))

        if mystic_pos is not None:
            logging.info("Found Mystic Bookmark")
            x, y = self.ScreenManager.get_position_of_template_match(
                mystic_pos)

            width, height = self.SecretShopTemplates.mystic["image"].shape[::-1]

            x1 = x + math.floor(width / 2) + 580
            y1 = y + math.floor(height / 2) + 10
            x2 = x + math.floor(width / 2) + 800
            y2 = y + math.floor(height / 2) + 55

            self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
                x1=x1, y1=y1, x2=x2, y2=y2, action="Click on Buy")

            self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
                x1=761, y1=605, x2=1059, y2=660, action="Click on Confirm Buy")

            self.mystic_count += 1
            self.check_bookmarks()

        if coven_pos is not None:
            logging.info("Found Covenant Bookmark")
            x, y = self.ScreenManager.get_position_of_template_match(coven_pos)

            width, height = self.SecretShopTemplates.covenant["image"].shape[::-1]

            x1 = x + math.floor(width / 2) + 580
            y1 = y + math.floor(height / 2) + 10
            x2 = x + math.floor(width / 2) + 800
            y2 = y + math.floor(height / 2) + 55

            self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
                x1=x1, y1=y1, x2=x2, y2=y2, action="Click on Buy")

            self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
                x1=761, y1=605, x2=1059, y2=660, action="Click on Confirm Buy")

            self.covenant_count += 1
            self.check_bookmarks()

    def scroll(self):
        x1, y1 = self.MathUtils.random_point_in_area(
            x1=750, y1=781, x2=1282, y2=845)
        x2, y2 = self.MathUtils.random_point_in_area(
            x1=701, y1=98, x2=1288, y2=174)

        self.DeviceManager.device.shell(
            f"input touchscreen swipe {x1} {y1} {x2} {y2} 400")

    def check_store(self):
        self.check_bookmarks()
        self.scroll()
        self.ScreenManager.sleep(1)
        self.check_bookmarks()

    def refresh(self):
        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=287, y1=808, x2=387, y2=838, action="Click on Refresh Button")
        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=878, y1=537, x2=986, y2=568, action="Click on Confirm Button")

        self.refreshes_count += 1

    def show_stats(self):
        comment = f"\nTotal Covenant: {str(self.covenant_count)}{' '*30}" + \
            f"\nTotal Mystic: {str(self.mystic_count)}{' '*30}" + \
            f"\nTotal Refreshes: {str(self.refreshes_count)}{' '*30}\n\n\n"
        previus_line = "\033[F"
        if self.refreshes_count == 1:
            print(f"\r{previus_line*2}{comment}")
        else:
            print(f"\r{previus_line*7}{comment}")
        pass

    def start_crafting(self):
        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=1024, y1=508, x2=1191, y2=579, action="Click on Craft x10 button")
        
        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=750, y1=624, x2=1027, y2=658, action="Click on Craft button")

        self.craft_and_extract_blues()

    def start_crafting_from_lobby(self):
        self.ScreenManager.ensure_not_on_sleep_mode_on_lobby()

        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=270, y1=225, x2=341, y2=284, action="Click on Sanctuary")
        
        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=1122, y1=686, x2=1307, y2=765, action="Click on Steel Workshop")
        
        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=430, y1=457, x2=559, y2=595, action="Click on Crafting")
        
        #tbd - add choose hunt to craft and equipment type (boots,swords,etc..)

        self.start_crafting()
