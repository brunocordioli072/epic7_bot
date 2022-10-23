from epic7_bot.commands.Command import Command
from epic7_bot.modules.Battle import Battle


class Hunt(Command):
    def __init__(self):
        self.Battle = Battle()

    def start(self):
        self.Battle.start_hunt()
