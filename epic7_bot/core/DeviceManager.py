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
        for d in devices:
            if self.ensure_device_has_epic7_app(d):
                device = d

        device.shell("wm size 1600x900")
        return device

    def ensure_device_has_epic7_app(self, device):
        res = device.shell("pm list packages -f")
        if "com.stove.epic7.google" in res:
            return True

    def ensure_adb_is_running(self):
        logging.info("Ensure ADB is running")
        subprocess.run(["adb", "start-server"])

    def ensure_device_is_connected(self):
        bluestacks_config_path = "C:\\ProgramData\\BlueStacks_nxt\\bluestacks.conf"
        with open(bluestacks_config_path, "r") as f:
            config = f.readlines()

        device_ports = set([])
        config = [x.strip().split("=", 1) for x in config if "=" in x]
        for c in config:
            if "adb_port" in c[0]:
                device_ports.add(c[1].replace('"', ""))

        for port in device_ports:
            subprocess.run(["adb", "connect", f"127.0.0.1:{port}"])
