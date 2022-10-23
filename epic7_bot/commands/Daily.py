from epic7_bot.commands.Command import Command
from epic7_bot.modules.Guild import Guild
from epic7_bot.modules.PetHouse import PetHouse
from epic7_bot.modules.Sanctuary import Sanctuary
from epic7_bot.modules.Summon import Summon


class Daily(Command):
    def __init__(self):
        self.Summon = Summon()
        self.PetHouse = PetHouse()
        self.Guild = Guild()
        self.Sanctuary = Sanctuary()

    def start(self):
        self.Summon.get_free_summon()
        self.PetHouse.get_free_pet_summon()
        self.Guild.do_daily_contributions()
        self.Sanctuary.do_sanctuary_routine()
