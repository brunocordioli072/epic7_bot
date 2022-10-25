"""

Usage:
    epic7 <command> [options]

All commands should be run when the game screen is in the lobby!

The most commonly used commands are:
    shop            Start secret shop auto buy
    arena           Start arena npc auto battle
    hunt            Start hunt auto battle
    daily           Start daily actions

Options:
    -h --help       Show this help message and exit
    -v --version    Show version and exit
    -c --current    Run command on current screen
"""

import sys
from time import sleep
from docopt import docopt
from sys import exit
from epic7_bot.processes.CheckConnection import CheckConnection
from epic7_bot.processes.CommandRunner import CommandRunner


def main():
    args = docopt(__doc__, version="1.0.0", options_first=False)

    commandRunner = CommandRunner(args)
    checkConnection = CheckConnection(commandRunner.pid)

    if args['<command>'] in [None]:
        sys.argv.append('-h')
        exit(main())
    elif args['<command>'] not in commandRunner.commands.keys():
        exit("%r is not a valid command." %
             args['<command>'])
    else:

        commandRunner.start()
        sleep(3)
        checkConnection.start()
        while True:
            if commandRunner.is_alive() is False:
                exit()
            sleep(1)
