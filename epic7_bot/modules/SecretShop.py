import logging
from epic7_bot.core.DeviceManager import DeviceManager
from epic7_bot.core.MathUtils import MathUtils
from epic7_bot.modules.Module import Module
from epic7_bot.templates.SecretShopTemplates import SecretShopTemplates


class SecretShop(Module):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.DeviceManager = DeviceManager()
        self.SecretShopTemplates = SecretShopTemplates()
        self.MathUtils = MathUtils()

        self.mystic_count = 0
        self.refreshes_count = 0
        self.covenant_count = 0
        self.bought = False

    def check_bookmarks(self):
        logging.info("Check Mystic and Covenant Bookmarks")
        mystic_pos = self.ScreenManager.match_template_on_screen(
            self.SecretShopTemplates.mystic)
        coven_pos = self.ScreenManager.match_template_on_screen(
            self.SecretShopTemplates.covenant)

        if mystic_pos is not None:
            logging.info("Found Mystic Bookmark")
            x, y = self.ScreenManager.get_position_of_template_match(
                mystic_pos)

            self.ScreenManager.click_position(x + 650, y + 50, 1)

            self.ScreenManager.match_template_on_screen_and_click_it(
                self.SecretShopTemplates.buy_button_mystic, 1)

            self.bought = True
            self.mystic_count += 1

        if coven_pos is not None:
            logging.info("Found Covenant Bookmark")
            x, y = self.ScreenManager.get_position_of_template_match(coven_pos)

            self.ScreenManager.click_position(x + 650, y + 50, 1)

            self.ScreenManager.match_template_on_screen_and_click_it(
                self.SecretShopTemplates.buy_button_covenant, 1)

            self.bought = True
            self.covenant_count += 1

    def scroll(self):
        x1, y1 = self.MathUtils.randomPoint(1200, 700)
        x2, y2 = self.MathUtils.randomPoint(1200, 300)

        self.DeviceManager.device.shell(
            f"input touchscreen swipe {x1} {y1} {x2} {y2} 300")

    def check_store(self):
        self.check_bookmarks()

        if self.bought is False:
            self.scroll()
            self.check_bookmarks()
        self.bought = False

    def refresh(self):
        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=287, y1=808, x2=387, y2=838, action="Click on Refresh Button")
        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
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

    def start_auto_buy_secret_shop(self):
        while True:
            self.check_store()
            self.refresh()
            self.show_stats()

    def start_auto_buy_secret_shop_from_lobby(self):
        self.ScreenManager.ensure_not_on_sleep_mode_on_lobby()

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=683, y1=204, x2=728, y2=246, action="Click on Bartender")
        self.start_auto_buy_secret_shop()
