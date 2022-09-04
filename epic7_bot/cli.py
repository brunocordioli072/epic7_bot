"""

usage:
    epic7 <command>
    epic7 [options]

The most commonly used commands are:
    shop            Start secret shop auto buy

options:
    -h --help       Show this help message and exit
    -v --version    Show version and exit
"""

from docopt import docopt
from subprocess import call
from sys import exit
import epic7_bot.auto_buy_secret_shop as auto_buy_secret_shop
import sys


def main():
    args = docopt(__doc__, version="1.0.0", options_first=True)

    if args['<command>'] == "shop":
        auto_buy_secret_shop.start_auto_buy_secret_shop()
    elif args['<command>'] in [None]:
        sys.argv.append('-h')
        exit(main())
    else:
        exit("%r is not a valid command." %
             args['<command>'])
