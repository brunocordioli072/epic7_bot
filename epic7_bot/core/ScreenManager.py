
import base64
import logging
import time
import cv2

import numpy as np
from epic7_bot.core.DeviceManager import DeviceManager
from epic7_bot.core.MathUtils import MathUtils
from epic7_bot.templates.Template import Template
from epic7_bot.utils.Singleton import Singleton


class ScreenManager(metaclass=Singleton):
    def __init__(self):
        self.MathUtils = MathUtils()
        self.DeviceManager = DeviceManager()

    def get_position_of_template_match(self, matchTemplate):
        position_x = np.unravel_index(
            matchTemplate.argmax(), matchTemplate.shape)[1]
        position_y = np.unravel_index(
            matchTemplate.argmax(), matchTemplate.shape)[0]
        return position_x, position_y

    def take_screenshot(self):
        png_screenshot_data = self.DeviceManager.device.shell(
            "screencap -p | busybox base64")
        png_screenshot_data = base64.b64decode(png_screenshot_data)
        nparr = np.frombuffer(png_screenshot_data, np.uint8)
        img = cv2.imdecode(nparr, 0)
        return img

    def take_screnshot_from_area(self, x1=None, x2=None, y1=None, y2=None):
        img = self.take_screenshot()
        if x1 != None and y1 != None and x2 != None and y2 != None:
            img = img[y1:y2, x1:x2]

        return img

    def match_template_on_screen(self, template: Template, percentage=0.6):
        image = self.take_screenshot()
        match = cv2.matchTemplate(
            image, template['image'], cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
        logging.debug(f"Checked {template['name']}, percentage: {max_val}")

        if max_val > percentage:
            return match
        else:
            return None

    def match_template_on_screen_area(self, x1, y1, x2, y2, template, percentage=0.55):
        image = self.take_screnshot_from_area(x1, x2, y1, y2)
        result = cv2.matchTemplate(
            image, template['image'], cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val > percentage:
            return max_val
        else:
            return None

    def match_template_on_screen_and_click_it(self, template, waitTime=0):
        time.sleep(waitTime)
        match = self.match_template_on_screen(template)
        if match is not None:
            position_x, position_y = self.get_position_of_template_match(match)
            x, y = self.MathUtils.randomPoint(position_x, position_y)
            self.DeviceManager.device.shell("input tap " +
                                            str(x) + " " + str(y))

    def check_if_images_changed(self, img1, img2, percentage=70):
        if img1 is None or img2 is None:
            return False
        res = cv2.absdiff(img1, img2)
        res = res.astype(np.uint8)
        result = (np.count_nonzero(res) * 100) / res.size
        return result >= percentage

    def click_position(self, position_x, position_y, waitTime, message=None):
        time.sleep(waitTime)
        x, y = self.MathUtils.randomPoint(position_x, position_y)
        self.DeviceManager.device.shell("input tap " + str(x) + " " + str(y))

    def click_middle(self, x1, y1, x2, y2):
        position_x, position_y = self.MathUtils.midpoint(x1, y1, x2, y2)
        self.click_position(position_x, position_y, waitTime=0)

    def click_middle_get_before_and_after_images_from_screen(self, x1, y1, x2, y2):
        beforeImage = self.take_screenshot()
        self.click_middle(x1, y1, x2, y2)
        time.sleep(2)
        afterImage = self.take_screenshot()
        return (beforeImage, afterImage)

    def click_middle_and_check_change_on_screen_retry(self, x1, y1, x2, y2, action=None):
        time.sleep(1)
        beforeImage, afterImage = None, None
        count = 0
        if action is not None:
            logging.debug(f"{action}")
        while self.check_if_images_changed(beforeImage, afterImage) is False and count < 2:
            beforeImage, afterImage = self.click_middle_get_before_and_after_images_from_screen(
                x1, y1, x2, y2)
            count += 1
        if count < 2 == False:
            logging.error(f"{action}")

        return count < 2

    def click_middle_get_before_and_after_images_from_area(self, x1, y1, x2, y2):
        beforeImage = self.take_screnshot_from_area(x1, x2, y1, y2)
        self.click_middle(x1, y1, x2, y2)
        time.sleep(3)
        afterImage = self.take_screnshot_from_area(x1, x2, y1, y2)
        return (beforeImage, afterImage)

    def click_middle_and_check_change_on_area_retry(self, x1, y1, x2, y2, action=None, percentage=20):
        time.sleep(1)
        beforeImage, afterImage = None, None
        count = 0
        if action is not None:
            logging.debug(f"{action}")
        while self.check_if_images_changed(beforeImage, afterImage, percentage) is False and count < 2:
            beforeImage, afterImage = self.click_middle_get_before_and_after_images_from_area(
                x1, y1, x2, y2)
            count += 1
        return count < 2
