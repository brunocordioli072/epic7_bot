from epic7_bot.core.ScreenManager import ScreenManager


class Module:
    def __init__(self, fastMode):
        self.ScreenManager = ScreenManager(fastMode)
