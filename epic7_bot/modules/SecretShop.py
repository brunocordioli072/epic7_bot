from epic7_bot.core.DeviceManager import DeviceManager
from epic7_bot.modules.Module import Module
from epic7_bot.templates.SecretShopTemplates import SecretShopTemplates


class SecretShop(Module):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.DeviceManager = DeviceManager()
        self.SecretShopTemplates = SecretShopTemplates()

        self.mystic_count = 0
        self.refreshes_count = 0
        self.covenant_count = 0
        self.bought = False

    def check_bookmarks(self):
        mystic_pos = self.ScreenManager.match_template_on_screen(
            self.SecretShopTemplates.mystic)
        coven_pos = self.ScreenManager.match_template_on_screen(
            self.SecretShopTemplates.covenant)

        if mystic_pos is not None:
            x, y = self.ScreenManager.get_position_of_template_match(
                mystic_pos)

            self.ScreenManager.click_position(x + 650, y + 50, 1)

            self.ScreenManager.match_template_on_screen_and_click_it(
                self.SecretShopTemplates.buy_button_mystic, 1)

            self.bought = True
            self.mystic_count += 1

        if coven_pos is not None:
            x, y = self.ScreenManager.get_position_of_template_match(coven_pos)

            self.ScreenManager.click_position(x + 650, y + 50, 1)

            self.ScreenManager.match_template_on_screen_and_click_it(
                self.SecretShopTemplates.buy_button_covenant, 1)

            self.bought = True
            self.covenant_count += 1

    def scroll(self):
        self.DeviceManager.device.shell(
            "input touchscreen swipe 1200 700 1200 300 300")

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
        print("="*20)
        print("Total Covenant: " + str(self.covenant_count))
        print("Total Mystic: " + str(self.mystic_count))
        print("Total Refreshes: " + str(self.refreshes_count))
        print("="*20)

    def start_auto_buy_secret_shop(self):
        try:
            while True:
                self.check_store()
                self.refresh()
                self.show_stats()
        except KeyboardInterrupt:
            print("ctrol-c pressed")
            exit(1)

    def start_auto_buy_secret_shop_from_lobby(self):
        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=894, y1=848, x2=935, y2=879, action="Click on Screen to Ensure not on Sleep Mode")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=747, y1=172, x2=802, y2=206, action="Click on Bartender")
        self.start_auto_buy_secret_shop()
