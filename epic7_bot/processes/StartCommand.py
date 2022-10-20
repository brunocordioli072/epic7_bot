
import multiprocessing
from epic7_bot.core.Logger import init_logger
from dotenv import load_dotenv
from epic7_bot.modules.SecretShop import SecretShop
from epic7_bot.modules.Arena import Arena
from epic7_bot.modules.Hunt import Hunt


class StartCommand(multiprocessing.Process):
    def __init__(self, args):
        multiprocessing.Process.__init__(self, daemon=True)
        self.args = args
        self.SecretShop = SecretShop()
        self.Arena = Arena()
        self.Hunt = Hunt()

    def run(self):
        load_dotenv()
        init_logger()

        if self.args['<command>'] == "shop":
            secretShop = SecretShop()
            secretShop.start_auto_buy_secret_shop()
        elif self.args['<command>'] == "arena":
            arena = Arena()
            arena.start_arena_npc_auto_battle()
        elif self.args['<command>'] == "hunt":
            hunt = Hunt()
            hunt.start_hunt()
        else:
            return
