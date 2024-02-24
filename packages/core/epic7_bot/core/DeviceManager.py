import logging
import subprocess
import sys
from time import sleep
from ppadb.client import Client
from epic7_bot.utils.Singleton import Singleton


class DeviceManager(metaclass=Singleton):
    def __init__(self):
        self.device = self.setup_device()

    def setup_device(self):
        self.ensure_adb_is_running()
        self.connect_devices_to_adb()

        client = Client(host="127.0.0.1", port=5037)
        devices = client.devices()
        if len(devices) == 0:
            logging.error("No device found, are you sure your bluestacks is open?")
            sys.exit()

        device = devices[0]
        devicesWithEpic7 = []
        for d in devices:
            hasEpic7 = self.ensure_device_has_epic7_app(d)
            devicesWithEpic7.append(hasEpic7)
            if hasEpic7:
                device = d
        if all(device is None for device in devicesWithEpic7):
            logging.error("No Epic Seven App found in devices.")

        device.shell("wm size 1600x900")
        return device

    def ensure_device_has_epic7_app(self, device):
        try:
            return device.is_installed("com.stove.epic7.google")
        except Exception as e:
            return None

    def ensure_adb_is_running(self):
        try:
            logging.info("Ensure ADB is running")
            sp = subprocess.Popen(
                ["adb", "start-server"],
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
            )
            sp.wait()
            sp.terminate()
        except Exception as e:
            logging.info("Something went wrong: " + str(e))

    def connect_devices_to_adb(self):
        bluestacks_config_path = "C:\\ProgramData\\BlueStacks_nxt\\bluestacks.conf"
        with open(bluestacks_config_path, "r") as f:
            config = f.readlines()

        device_ports = set([])
        config = [x.strip().split("=", 1) for x in config if "=" in x]
        for c in config:
            if "adb_port" in c[0]:
                device_ports.add(c[1].replace('"', ""))

        for port in device_ports:
            subprocess.Popen(
                ["adb", "connect", f"127.0.0.1:{port}"],
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
            ).wait()
