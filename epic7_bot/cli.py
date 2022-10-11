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

from docopt import docopt
from subprocess import call
from sys import exit
from epic7_bot.auto_buy_secret_shop import start_auto_buy_secret_shop
from epic7_bot.arena import start_arena_npc_auto_battle
from epic7_bot.utils.devices import setup_device
import sys


def main():
    args = docopt(__doc__, version="1.0.0", options_first=True)

    if args['<command>'] != None:
        setup_device()
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
