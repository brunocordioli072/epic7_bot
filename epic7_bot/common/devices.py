from ppadb.client import Client
import epic7_bot.common.config as config


def setup_device():
    client = Client(host="127.0.0.1", port=5037)
    device = client.devices()[0]
    device.shell("wm size 1600x900")
    config.device = device
