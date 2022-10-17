"""

usage:
    epic7 <command>
    epic7 [options]

The most commonly used commands are:
    shop            Start secret shop auto buy
    arena:npc       Start arena npc auto battle

options:
    -h --help       Show this help message and exit
    -v --version    Show version and exit
"""

import threading
from time import sleep
from docopt import docopt
from sys import exit
from epic7_bot.auto_buy_secret_shop import start_auto_buy_secret_shop
from epic7_bot.arena import start_arena_npc_auto_battle
from epic7_bot.common.connection import start_checking_connection_problem
from epic7_bot.common.devices import setup_device
from epic7_bot.common.logger import init_logger
import epic7_bot.common.config as config
from dotenv import load_dotenv
import sys


stopped_start_checking_connection_problem = False


def main():
    def task():
        args = docopt(__doc__, version="1.0.0", options_first=True)

        if args['<command>'] != None:
            load_dotenv()
            init_logger()
            setup_device()
            threading.Thread(
                target=start_checking_connection_problem, daemon=True).start()
        if args['<command>'] == "shop":
            start_auto_buy_secret_shop()
        elif args['<command>'] == "arena:npc":
            start_arena_npc_auto_battle()
        elif args['<command>'] in [None]:
            sys.argv.append('-h')
            exit(main())
        else:
            exit("%r is not a valid command." %
                 args['<command>'])

    thread = threading.Thread(
        target=task, daemon=True)
    thread.start()
    while True:
        if config.is_checking_connection_problem is False:
            exit()
        sleep(1)
