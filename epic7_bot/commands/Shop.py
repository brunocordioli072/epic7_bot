from epic7_bot.commands.Command import Command
from epic7_bot.modules.SecretShop import SecretShop


class Shop(Command):
    def __init__(self):
        self.SecretShop = SecretShop()

    def start(self):
        self.SecretShop.start_auto_buy_secret_shop()
