from epic7_bot.commands.Command import Command
from epic7_bot.modules.Battle import Battle


class Hunt(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.Battle = Battle()

    def start(self):
        if self.currentScreen == False:
            self.Battle.start_hunt_from_lobby()
        else:
            self.Battle.start_hunt()
