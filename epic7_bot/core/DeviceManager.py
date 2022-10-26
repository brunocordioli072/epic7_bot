import logging
import subprocess
from time import sleep
from ppadb.client import Client
from epic7_bot.utils.Singleton import Singleton


class DeviceManager(metaclass=Singleton):
    def __init__(self):
        self.device = self.setup_device()

    def setup_device(self):
        self.ensure_adb_is_running()
        client = Client(host="127.0.0.1", port=5037)
        devices = client.devices()
        if len(devices) == 0:
            logging.error("No device found")
            self.ensure_device_is_connected()
            sleep(2)
            devices = client.devices()

        device = devices[0]
        device.shell("wm size 1600x900")
        return device

    def ensure_adb_is_running(self):
        logging.info("Ensure ADB is running")
        subprocess.run(["adb", "start-server"])

    def ensure_device_is_connected(self):
        logging.info("Trying to connect to a Nox emulator device")
        subprocess.run(["adb", "connect", "127.0.0.1:62001"])
        logging.info("Trying to connect to a Bluestacks emulator device")
        subprocess.run(["adb", "connect", "127.0.0.1:5555"])
