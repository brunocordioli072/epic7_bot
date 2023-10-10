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
    -f --fast       Run command on fast mode (not stable)
"""

import sys
from time import sleep
from docopt import docopt
from sys import exit
from processes.CheckConnection import CheckConnection
from processes.CommandRunner import CommandRunner
from processes.CommandRunner import CommandRunner
from processes.DispatchMissionChecker import DispatchMissionChecker


def main():
    try:
        args = docopt(__doc__, version="1.0.0", options_first=False)

        commandRunner = CommandRunner(args)
        dispatchMissionChecker = DispatchMissionChecker(commandRunner.pid)
        checkConnection = CheckConnection(commandRunner.pid)

        if args["<command>"] in [None]:
            sys.argv.append("-h")
            exit(main())
        elif args["<command>"] not in commandRunner.commands.keys():
            exit("%r is not a valid command." % args["<command>"])
        else:
            commandRunner.start()
            sleep(3)
            checkConnection.start()
            dispatchMissionChecker.start()
            while True:
                if commandRunner.is_alive() is False:
                    print("\n\nJob Finished, bot closing")

                    exit()
                sleep(1)
    except KeyboardInterrupt:
        print("\n\nCtrol-C pressed, bot closing")

        while True:
            if commandRunner.is_alive():
                commandRunner.terminate()
            if checkConnection.is_alive():
                checkConnection.terminate()
            if (
                commandRunner.is_alive() is not True
                and commandRunner.is_alive() is not True
            ):
                exit()
            sleep(0.5)
