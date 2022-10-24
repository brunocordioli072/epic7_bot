
import multiprocessing
import subprocess
from epic7_bot.commands.Command import Command
from epic7_bot.core.Logger import init_logger
from dotenv import load_dotenv
from epic7_bot.modules.SecretShop import SecretShop
from epic7_bot.modules.Arena import Arena
from epic7_bot.modules.Battle import Battle
from epic7_bot.commands.Daily import Daily
from epic7_bot.commands.Hunt import Hunt
from epic7_bot.commands.Arena import Arena
from epic7_bot.commands.Shop import Shop


class CommandRunner(multiprocessing.Process):
    def __init__(self, args):
        multiprocessing.Process.__init__(self, daemon=True)
        self.args = args
        self.commands: dict[str, type[Command]] = {
            "daily": Daily,
            "hunt": Hunt,
            "arena": Arena,
            "shop": Shop,
        }

    def run(self):
        load_dotenv()
        init_logger()
        self.ensure_adb_is_running()

        command = self.commands[self.args['<command>']]
        command(currentScreen=self.args['--current']).start()

    def ensure_adb_is_running(self):
        subprocess.run(["adb", "start-server"])
