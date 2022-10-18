"""

usage:
    epic7 <command>
    epic7 [options]

The most commonly used commands are:
    shop            Start secret shop auto buy
    arena           Start arena npc auto battle
    hunt            Start hunt auto battle

options:
    -h --help       Show this help message and exit
    -v --version    Show version and exit
"""

import multiprocessing
from time import sleep
from docopt import docopt
from sys import exit
from epic7_bot.auto_buy_secret_shop import start_auto_buy_secret_shop
from epic7_bot.arena import start_arena_npc_auto_battle
from epic7_bot.hunt import start_hunt
from epic7_bot.common.connection import start_checking_connection_problem
from epic7_bot.common.devices import setup_device
from epic7_bot.common.logger import init_logger
import epic7_bot.common.config as config
from dotenv import load_dotenv
import sys


def task(args):
    load_dotenv()
    init_logger()
    setup_device()

    if args['<command>'] == "shop":
        start_auto_buy_secret_shop()
    elif args['<command>'] == "arena":
        start_arena_npc_auto_battle()
    elif args['<command>'] == "hunt":
        start_hunt()
    else:
        return


def main():
    args = docopt(__doc__, version="1.0.0", options_first=True)

    if args['<command>'] in [None]:
        sys.argv.append('-h')
        exit(main())
    elif args['<command>'] not in ["shop", "arena", "hunt"]:
        exit("%r is not a valid command." %
             args['<command>'])
    else:
        thread1 = multiprocessing.Process(
            target=task, args=[args], daemon=True)
        thread1.start()
        sleep(3)
        thread2 = multiprocessing.Process(
            target=start_checking_connection_problem, args=[thread1.pid], daemon=True)
        thread2.start()
        while True:
            if thread1.is_alive() is False:
                exit()
            if config.is_checking_connection_problem is False:
                exit()
            sleep(1)
