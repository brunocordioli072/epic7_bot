"""

usage:
    epic7 <command>
    epic7 [options]

The most commonly used commands are:
    shop            Start secret shop auto buy
    arena           Start arena npc auto battle
    hunt            Start hunt auto battle
    daily           Start daily actions

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
    startCommand = StartCommand(args)
    checkConnection = CheckConnection(startCommand.pid)

    if args['<command>'] in [None]:
        sys.argv.append('-h')
        exit(main())
    elif args['<command>'] not in startCommand.commands.keys():
        exit("%r is not a valid command." %
             args['<command>'])
    else:

        startCommand.start()
        sleep(3)
        checkConnection.start()
        while True:
            if startCommand.is_alive() is False:
                exit()
            sleep(1)
