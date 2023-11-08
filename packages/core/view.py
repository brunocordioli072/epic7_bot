from typing import Any, Dict
from tinydb import TinyDB, where
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

    def start_command(self, args):
        if self.runningCommand is not None:
            self.stop_running_command()
        self.runningCommand = CommandRunner(args)
        self.runningCommand.start()

    def start_shop(self):
        args = {
            "<command>": "shop",
            "--current": False,
            "--fast": False,
        }
        self.start_command(args)

    def start_hunt(self):
        args = {"<command>": "hunt", "--current": False, "--fast": False}
        self.start_command(args)

    def start_arena(self):
        args = {"<command>": "arena", "--current": False, "--fast": False}
        self.start_command(args)

    def start_daily(self):
        args = {"<command>": "daily", "--current": False, "--fast": False}
        self.start_command(args)

    def stop_running_command(self):
        self.runningCommand.terminate()

    def get_logs(self):
        try:
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            f = open(ROOT_DIR + "\logs", "r")
            return f.read()
        except BaseException as e:
            raise e
        
    def get_summary(self, module):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        db = TinyDB(ROOT_DIR + "\\db.json")
        table = db.table(module)
        contents = table.all()
        if len(contents) > 0:
            return contents[0]

if __name__ == "__main__":
    api = Api()

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    if os.path.exists(ROOT_DIR + "\\logs") is not True:
        with open(ROOT_DIR + "\\logs", "w") as log:
            pass

    if os.path.exists(ROOT_DIR + "\\db.json") is not True:
        with open(ROOT_DIR + "\\db.json", "w") as log:
            pass
    
    webview.create_window(
        "Epic7 Bot",
        "dist-app/index.html",
        js_api=api,
        min_size=(600, 470),
    )
    webview.start(debug=True)
