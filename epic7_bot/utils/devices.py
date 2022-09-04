from ppadb.client import Client

device = None


def setup_device():
    client = Client(host="127.0.0.1", port=5037)
    d = client.devices()[0]
    global device
    device = d
    device.shell("wm size 1536x864")


def get_device():
    return device
