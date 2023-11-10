from tinydb import TinyDB
import webview
import requests
import os
import multiprocessing
from epic7_bot.processes.CommandRunner import CommandRunner

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CURRENT_APP_VERSION = "v2.0.5-beta"

class Api:
    def __init__(self) -> None:
        self.runningCommand = None
        multiprocessing.set_start_method("spawn", force=True)
        multiprocessing.freeze_support()

    def get_version(self):
        response = requests.get("https://api.github.com/repos/brunocordioli072/epic7_bot/releases/latest")
        return {'current_app_version': CURRENT_APP_VERSION, 'latest_app_version': response.json()["name"]}


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
            f = open(ROOT_DIR + "\logs", "r")
            return f.read()
        except BaseException as e:
            raise e
        
    def get_summary(self, table):
        db = TinyDB(ROOT_DIR + "\\db.json")
        table = db.table(table)
        contents = table.all()
        if len(contents) > 0:
            return contents[0]

if __name__ == "__main__":
    # Create logs file
    if os.path.exists(ROOT_DIR + "\\logs") is not True:
        with open(ROOT_DIR + "\\logs", "w") as log:
            pass
    # Create db file
    if os.path.exists(ROOT_DIR + "\\db.json") is not True:
        with open(ROOT_DIR + "\\db.json", "w") as db:
            pass
    
    api = Api()
    webview.create_window(
        "Epic7 Bot",
        "dist-app/index.html",
        js_api=api,
        min_size=(600, 470),
    )
    webview.start(debug=False)
