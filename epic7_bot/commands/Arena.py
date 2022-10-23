from epic7_bot.commands.Command import Command
from epic7_bot.modules.Arena import Arena as ArenaM


class Arena(Command):
    def __init__(self):
        self.Arena = ArenaM()

    def start(self):
        self.Arena.start_arena_npc_auto_battle()
