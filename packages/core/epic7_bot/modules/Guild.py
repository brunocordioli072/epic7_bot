from time import sleep
from epic7_bot.modules.Module import Module


class Guild(Module):
    def __init__(self):
        super(self.__class__, self).__init__()

    def world_boss_rotation(self):
        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1083, y1=808, x2=1182, y2=848, action="Click on Ready Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1221, y1=739, x2=1390, y2=774, action="Click on Select Team Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1249, y1=805, x2=1460, y2=838, action="Click on Team Formation Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=120, y1=794, x2=287, y2=838, action="Click on Auto Assign Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1104, y1=804, x2=1189, y2=842, action="Click on Start Button")

        sleep(10)

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1318, y1=25, x2=1407, y2=62, action="Click on Skip Button")

        sleep(10)

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=735, y1=758, x2=873, y2=798, action="Click on Open All Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=735, y1=758, x2=873, y2=798, action="Click on Confirm Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1388, y1=806, x2=1505, y2=844, action="Click on Confirm Button Again")

    def do_daily_contributions(self):
        self.ScreenManager.ensure_not_on_sleep_mode_on_lobby()

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=604, y1=812, x2=679, y2=881, action="Click on Guild Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=759, y1=797, x2=844, y2=833, action="Click on Tap to Close")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1064, y1=792, x2=1186, y2=848, action="Click on Daily Reward")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=759, y1=797, x2=844, y2=833, action="Click on Tap to Close")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1332, y1=249, x2=1476, y2=294, action="Click on Battlefield Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=408, y1=509, x2=614, y2=556, action="Click on World Boss Button")

        self.world_boss_rotation()

        self.world_boss_rotation()

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=34, y1=12, x2=225, y2=67, action="Go Back to Clan Lobby")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1336, y1=502, x2=1441, y2=535, action="Click on Donate Section")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1041, y1=528, x2=1155, y2=559, action="Click on Donate Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=720, y1=649, x2=878, y2=683, action="Click on Tap to Close")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1046, y1=799, x2=1159, y2=839, action="Click on Donate Button Again")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=720, y1=649, x2=878, y2=683, action="Click on Tap to Close")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=34, y1=12, x2=225, y2=67, action="Go Back to Lobby")
