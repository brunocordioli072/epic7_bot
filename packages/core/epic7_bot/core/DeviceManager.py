import logging
import subprocess
import sys
from time import sleep
from ppadb.client import Client
from epic7_bot.utils.Singleton import Singleton
import os
import re
import win32api

class DeviceManager(metaclass=Singleton):
    def __init__(self):
        self.device = self.setup_device()

    def setup_device(self):
        self.ensure_adb_is_running()

        client = Client(host="127.0.0.1", port=5037)
        devices = client.devices()
        if len(devices) == 0:
            logging.error("No device found, are you sure your bluestacks is open?")
            sys.exit()
        logging.info(f"Found {len(devices)} devices")

        device = devices[0]
        logging.info(f"Connected to {device.serial}")

        devicesWithEpic7 = []
        for d in devices:
            hasEpic7 = self.ensure_device_has_epic7_app(d)
            devicesWithEpic7.append(hasEpic7)
            if hasEpic7:
                device = d
        if all(device is None for device in devicesWithEpic7):
            logging.error("No Epic Seven App found in devices.")
        logging.info(f"Checked if device {device.serial} has Epic Seven App")


        device.shell("wm size 1600x900")
        logging.info(f"Set device {device.serial} size to 1600x900")
        return device

    def ensure_device_has_epic7_app(self, device):
        try:
            return device.is_installed("com.stove.epic7.google")
        except Exception as e:
            return None

    def ensure_adb_is_running(self):
        logging.info("Ensure ADB is running")
        sp = subprocess.Popen(
            ["adb", "start-server"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        sp.wait(timeout=5)
        if sp.returncode != 0:
            logging.error(f"ensure_adb_is_running - Something went wrong: {str(sp.stderr.read().decode())}") 

        sp.terminate()