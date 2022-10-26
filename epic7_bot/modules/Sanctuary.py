from time import sleep
from epic7_bot.modules.Module import Module


class Sanctuary(Module):
    def __init__(self):
        super(self.__class__, self).__init__()

    def do_sanctuary_routine(self):
        self.ScreenManager.ensure_not_on_sleep_mode_on_lobby()

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=259, y1=240, x2=359, y2=301, action="Click on Sanctuary Button")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=708, y1=596, x2=876, y2=661, action="Click on Heart of Orbis Reward")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=722, y1=608, x2=882, y2=647, action="Click on Tap to Close")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=351, y1=365, x2=505, y2=388, action="Click on Forest of Souls")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=663, y1=157, x2=748, y2=223, action="Click on Penguin Nest Reward")

        sleep(2)

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=722, y1=608, x2=882, y2=647, action="Click on Tap to Close")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=1251, y1=276, x2=1320, y2=322, action="Click on Spirit Well Reward")

        sleep(2)

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=722, y1=608, x2=882, y2=647, action="Click on Tap to Close")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=915, y1=508, x2=989, y2=573, action="Click on MolaGora Farm Reward")

        sleep(2)

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=722, y1=608, x2=882, y2=647, action="Click on Tap to Close")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=34, y1=12, x2=225, y2=67, action="Go Back to Sanctuary")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=34, y1=12, x2=225, y2=67, action="Go Back to Lobby")
