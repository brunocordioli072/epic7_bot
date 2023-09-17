from epic7_bot.commands.Command import Command
from epic7_bot.modules.Equipment import Equipment


class Crafting(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.Equipment = Equipment(self.fastMode)

    def start(self):
        if self.currentScreen == False:
            self.Equipment.start_crafting_from_lobby()
        else:
            self.Equipment.start_crafting()
