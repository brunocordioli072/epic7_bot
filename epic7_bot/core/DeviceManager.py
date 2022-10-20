from ppadb.client import Client


class DeviceManager:
    def __init__(self):
        self.device = self.setup_device()

    def setup_device(self):
        client = Client(host="127.0.0.1", port=5037)
        device = client.devices()[0]
        device.shell("wm size 1600x900")
        return device
