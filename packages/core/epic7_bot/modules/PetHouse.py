from time import sleep
from epic7_bot.modules.Module import Module


class PetHouse(Module):
    def __init__(self):
        super(self.__class__, self).__init__()

    def get_free_pet_summon(self):
        self.ScreenManager.ensure_not_on_sleep_mode_on_lobby()

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=481, y1=795, x2=582, y2=877, action="Click on Pet House Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=1096, y1=795, x2=1197, y2=839, action="Click on First Adopt Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=810, y1=747, x2=923, y2=786, action="Click on Second Adopt Button")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=699, y1=841, x2=878, y2=879, action="Click on Tap to Close")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=699, y1=841, x2=878, y2=879, action="Click on Tap to Close Again")

        self.ScreenManager.random_click_on_area_and_check_change_retry(
            x1=34, y1=12, x2=225, y2=67, action="Go Back to Lobby")
