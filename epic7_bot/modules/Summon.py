from time import sleep
from epic7_bot.modules.Module import Module


class Summon(Module):
    def __init__(self):
        super(self.__class__, self).__init__()

    def get_free_summon(self):

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=894, y1=848, x2=935, y2=879, action="Click on Screen to Ensure not on Sleep Mode")

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=245, y1=801, x2=349, y2=878, action="Click on Summon Lobby Button")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=1232, y1=649, x2=1478, y2=685, action="Click on Covenant Summon Button")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=433, y1=795, x2=554, y2=851, action="Click on Free Summon Button")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=889, y1=636, x2=1010, y2=678, action="Click on Confirm Button")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=702, y1=453, x2=794, y2=508, action="Click on Middle of Screen")

        sleep(4)

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=143, y1=809, x2=251, y2=842, action="Click on Back Button")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=34, y1=12, x2=225, y2=67, action="Go Back to Lobby")