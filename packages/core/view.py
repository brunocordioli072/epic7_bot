import webview
import os
import multiprocessing
from epic7_bot.processes.CommandRunner import CommandRunner

"""
An example of serverless app architecture
"""


class Api:
    def __init__(self) -> None:
        self.runningCommand = None
        multiprocessing.set_start_method("spawn", force=True)
        multiprocessing.freeze_support()

    def startShop(self):
        args = {"<command>": "shop", "--current": False, "--fast": False}
        self.runningCommand = CommandRunner(args)
        self.runningCommand.start()

    def startHunt(self):
        args = {"<command>": "hunt", "--current": False, "--fast": False}
        self.runningCommand = CommandRunner(args)
        self.runningCommand.start()

    def startArena(self):
        args = {"<command>": "arena", "--current": False, "--fast": False}
        self.runningCommand = CommandRunner(args)
        self.runningCommand.start()

    def startDaily(self):
        args = {"<command>": "daily", "--current": False, "--fast": False}
        self.runningCommand = CommandRunner(args)
        self.runningCommand.start()

    def stopRunningCommand(self):
        self.runningCommand.terminate()

    def getLogs(self):
        try:
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            f = open(ROOT_DIR + "\logs", "r")
            return f.read()
        except BaseException as e:
            raise e


if __name__ == "__main__":
    api = Api()

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    if os.path.exists(ROOT_DIR + "\\logs") is not True:
        with open(ROOT_DIR + "\\logs", "w") as log:
            pass

    webview.create_window(
        "Epic7 Bot",
        "dist-app/index.html",
        js_api=api,
        min_size=(600, 470),
    )
    webview.start(debug=False)
