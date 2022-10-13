import time
from epic7_bot.templates import Template
from epic7_bot.utils.devices import get_device
import base64
import time
import cv2
import io
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
    print(f"Checked {template['name']}, percentage: {max_val}")

    if max_val > 0.6:
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


def take_screnshot(x1=None, x2=None, y1=None, y2=None):

    device = get_device()
    png_screenshot_data = device.shell("screencap -p | busybox base64")
    png_screenshot_data = base64.b64decode(png_screenshot_data)
    nparr = np.frombuffer(png_screenshot_data, np.uint8)
    img = cv2.imdecode(nparr, 0)
    if x1 != None and y1 != None and x2 != None and y2 != None:
        img = img[y1:y2, x1:x2]

    return img


def check_if_screen_changed(img1, img2):
    if img1 is None or img2 is None:
        return False
    res = cv2.absdiff(img1, img2)
    res = res.astype(np.uint8)
    percentage = (np.count_nonzero(res) * 100) / res.size
    print(f"percentage: {percentage}")
    return percentage >= 90


def midpoint(x1, y1, x2, y2):
    return ((x1 + x2)/2, (y1 + y2)/2)


def check_change_on_area(x1, y1, x2, y2, template):
    image = take_screnshot(x1, x2, y1, y2)
    result = cv2.matchTemplate(
        image, template['image'], cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(f"Checked {template['name']}, percentage: {max_val}")
    if max_val > 0.55:
        return result
    else:
        return None


def click_middle_and_check_change(x1, y1, x2, y2):
    beforeImage = take_screnshot(x1, x2, y1, y2)
    position_x, position_y = midpoint(x1, y1, x2, y2)
    click_position(position_x, position_y, waitTime=0)
    time.sleep(2)
    afterImage = take_screnshot(x1, x2, y1, y2)
    return (beforeImage, afterImage)


def click_middle_and_check_change_retry(x1, y1, x2, y2):
    time.sleep(1)
    beforeImage, afterImage = None, None
    count = 0
    while check_if_screen_changed(beforeImage, afterImage) is False and count < 2:
        beforeImage, afterImage = click_middle_and_check_change(x1, y1, x2, y2)
        count += 1
    return count < 2
