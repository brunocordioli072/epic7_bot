import logging
import subprocess
from ppadb.client import Client
from epic7_bot.utils.Singleton import Singleton


class DeviceManager(metaclass=Singleton):
    def __init__(self):
        self.device = self.setup_device()

    def setup_device(self):
        self.ensure_adb_is_running()
        client = Client(host="127.0.0.1", port=5037)
        device = client.devices()[0]
        device.shell("wm size 1600x900")
        return device

    def ensure_adb_is_running(self):
        logging.debug("Ensure ADB is running")
        subprocess.run(["adb", "start-server"])
