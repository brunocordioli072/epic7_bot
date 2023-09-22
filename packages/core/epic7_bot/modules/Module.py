from epic7_bot.core.ScreenManager import ScreenManager


class Module:
    def __init__(self, fastMode=False):
        self.ScreenManager = ScreenManager(fastMode)
