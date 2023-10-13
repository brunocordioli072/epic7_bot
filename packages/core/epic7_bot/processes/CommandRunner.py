import multiprocessing
import os
from epic7_bot.commands.Command import Command
from epic7_bot.core.Logger import get_log_level, init_logger
from dotenv import load_dotenv
from epic7_bot.modules.Arena import Arena
from epic7_bot.commands.Daily import Daily
from epic7_bot.commands.Hunt import Hunt
from epic7_bot.commands.Arena import Arena
from epic7_bot.commands.Shop import Shop
from epic7_bot.commands.Crafting import Crafting


class CommandRunner(multiprocessing.Process):
    def __init__(self, args):
        multiprocessing.Process.__init__(self, daemon=True)
        self.args = args
        self.commands: dict[str, type[Command]] = {
            "daily": Daily,
            "hunt": Hunt,
            "arena": Arena,
            "shop": Shop,
            "crafting": Crafting,
        }

    def run(self):
        try:
            load_dotenv()
            init_logger()

            command = self.commands[self.args["<command>"]]
            command(
                currentScreen=self.args["--current"], fastMode=self.args["--fast"]
            ).start()
        except BaseException as e:
            if get_log_level() == "DEBUG":
                raise e
            else:
                pass

    def terminate(self) -> None:
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        if os.path.exists(ROOT_DIR + "\\logs"):
            os.remove(ROOT_DIR + "\\logs")
        return super().terminate()
