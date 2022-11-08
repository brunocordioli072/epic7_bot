import base64
import cv2
import numpy as np
from ppadb.client import Client

device = None
image = None
filename = "test.png"


def setup_device():
    client = Client(host="127.0.0.1", port=5037)
    d = client.devices()[0]
    global device
    device = d
    device.shell("wm size 1536x864")


def get_device():
    return device


def take_screnshot_from_area(x1=None, x2=None, y1=None, y2=None):
    png_screenshot_data = device.shell("screencap -p | busybox base64")
    png_screenshot_data = base64.b64decode(png_screenshot_data)
    nparr = np.frombuffer(png_screenshot_data, np.uint8)
    img = cv2.imdecode(nparr, 0)
    if x1 != None and y1 != None and x2 != None and y2 != None:
        img = img[y1:y2, x1:x2]

    return img


coords = []


def get_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.drawMarker(image, (int(x), int(y)), color=(0, 255, 0))
        coords.append(x)
        coords.append(y)
        if len(coords) > 2:
            img = take_screnshot_from_area(
                x1=coords[0], y1=coords[1], x2=coords[2], y2=coords[3])
            cv2.imwrite("test-cut.png", img)
            print(
                f"x1={coords[0]}, y1={coords[1]}, x2={coords[2]}, y2={coords[3]}")


def take_screnshot():
    png_screenshot_data = device.shell("screencap -p | busybox base64")
    png_screenshot_data = base64.b64decode(png_screenshot_data)
    with open(filename, "wb") as fp:
        fp.write(png_screenshot_data)


setup_device()
device = get_device()

take_screnshot()
cv2.namedWindow('image')
cv2.setMouseCallback("image", get_mouse)


image = cv2.imread(filename)
while (1):
    cv2.imshow('image', image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
