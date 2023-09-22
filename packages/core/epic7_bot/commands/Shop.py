from epic7_bot.commands.Command import Command
from epic7_bot.modules.SecretShop import SecretShop


class Shop(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.SecretShop = SecretShop(self.fastMode)

    def start(self):
        if self.currentScreen == False:
            self.SecretShop.start_auto_buy_secret_shop_from_lobby()
        else:
            self.SecretShop.start_auto_buy_secret_shop()
