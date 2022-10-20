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

import sys
from time import sleep
from docopt import docopt
from sys import exit
from epic7_bot.processes.CheckConnection import CheckConnection
from epic7_bot.processes.StartCommand import StartCommand


def main():
    args = docopt(__doc__, version="1.0.0", options_first=True)

    if args['<command>'] in [None]:
        sys.argv.append('-h')
        exit(main())
    elif args['<command>'] not in ["shop", "arena", "hunt"]:
        exit("%r is not a valid command." %
             args['<command>'])
    else:
        thread1 = StartCommand(args)
        thread1.start()
        sleep(3)
        thread2 = CheckConnection(thread1.pid)
        thread2.start()
        while True:
            if thread1.is_alive() is False:
                exit()
            sleep(1)
