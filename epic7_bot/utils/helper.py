import time
from epic7_bot.templates import Template
from epic7_bot.utils.devices import get_device
import base64
import time
import cv2
import numpy as np
from random import random
import math


def randomPoint(aroundX, aroundY, scale=1, density=2):
    angle = random()*2*math.pi

    x = random()
    if x == 0:
        x = 0.0000001

    distance = scale * (pow(x, -1.0/density) - 1)
    return (aroundX + distance * math.sin(angle),
            aroundY + distance * math.cos(angle))


def click_position(position_x, position_y, waitTime, message=None):
    time.sleep(waitTime)
    # if message is not None:
    #     logging.info(message)
    x, y = randomPoint(position_x, position_y)
    device = get_device()
    device.shell("input tap " + str(x) + " " + str(y))
    # logging.info('Input tap at position: [ %s , %s ]',  str(x), str(y))


def get_position_of_image(result):
    position_x = np.unravel_index(result.argmax(), result.shape)[1]
    position_y = np.unravel_index(result.argmax(), result.shape)[0]
    return position_x, position_y


def check_image(template: Template):
    device = get_device()
    png_screenshot_data = device.shell("screencap -p | busybox base64")
    png_screenshot_data = base64.b64decode(png_screenshot_data)
    images = cv2.imdecode(np.frombuffer(png_screenshot_data, np.uint8), 0)
    result = cv2.matchTemplate(images, template['image'], cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print(f"Checked {template['name']}, percentage: {max_val}")

    if max_val > 0.7:
        return result
    else:
        return None


def click_image(template, waitTime=0):
    time.sleep(waitTime)
    device = get_device()
    result = check_image(template)
    if result is not None:
        position_x = np.unravel_index(result.argmax(), result.shape)[1]
        position_y = np.unravel_index(result.argmax(), result.shape)[0]
        x, y = randomPoint(position_x, position_y)
        device.shell("input tap " +
                     str(x) + " " + str(y))
        # logging.info('Found at position: [ %s , %s ]', str(
        #     x), str(y))
