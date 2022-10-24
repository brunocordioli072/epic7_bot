from epic7_bot.commands.Command import Command
from epic7_bot.modules.Arena import Arena as ArenaM


class Arena(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.Arena = ArenaM()

    def start(self):
        if self.currentScreen == False:
            self.Arena.start_arena_npc_auto_battle_from_lobby()
        else:
            self.Arena.start_arena_npc_auto_battle()
