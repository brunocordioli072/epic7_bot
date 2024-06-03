
import base64
import logging
import time
import cv2
import random

from cv2 import Mat

import numpy as np
from epic7_bot.core.DeviceManager import DeviceManager
from epic7_bot.core.MathUtils import MathUtils
from epic7_bot.templates.Template import Template
from epic7_bot.utils.Singleton import Singleton


class ScreenManager(metaclass=Singleton):
    def __init__(self, fastMode: bool = False):
        self.MathUtils = MathUtils()
        self.DeviceManager = DeviceManager()
        self.fastMode = fastMode

    def sleep(self, waitTime: float):
        sleep_time = random.uniform(
            0.5, 0.8) if self.fastMode else random.uniform(waitTime, waitTime + 1)
        time.sleep(sleep_time)

    def get_position_of_template_match(self, matchTemplate: np.ndarray) -> tuple[int, int]:
        position_y, position_x = np.unravel_index(
            matchTemplate.argmax(), matchTemplate.shape)
        return position_x, position_y

    def take_screenshot(self) -> np.ndarray:
        png_screenshot_data = self.DeviceManager.device.shell(
            "screencap -p | busybox base64")
        png_screenshot_data = base64.b64decode(png_screenshot_data)
        nparr = np.frombuffer(png_screenshot_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
        return img

    def take_screenshot_from_area(self, x1: int = None, x2: int = None, y1: int = None, y2: int = None) -> np.ndarray:
        img = self.take_screenshot()
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            img = img[y1:y2, x1:x2]
        return img

    def match_template_on_screen(self, template: Template, percentage: float = 0.6) -> np.ndarray:
        image = self.take_screenshot()
        match = cv2.matchTemplate(
            image, template['image'], cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(match)
        logging.debug(
            f"match_template_on_screen {template['name']}, percentage: {max_val}, {max_val > percentage}")
        return match if max_val > percentage else None

    def match_template_on_screen_area(self, x1: int, y1: int, x2: int, y2: int, template: Template, percentage: float = 0.55) -> float:
        image = self.take_screenshot_from_area(x1, x2, y1, y2)
        result = cv2.matchTemplate(
            image, template['image'], cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        logging.debug(
            f"match_template_on_screen_area {template['name']}, percentage: {max_val}, {max_val > percentage}")
        return max_val if max_val > percentage else None

    def match_template_on_screen_and_click_it(self, template: Template, waitTime: float = 0):
        self.sleep(random.uniform(waitTime, waitTime + 0.5))
        match = self.match_template_on_screen(template)
        if match is not None:
            position_x, position_y = self.get_position_of_template_match(match)
            x, y = self.MathUtils.randomPoint(position_x, position_y)
            self.DeviceManager.device.shell(f"input tap {x} {y}")

    def check_if_images_changed(self, img1: np.ndarray, img2: np.ndarray, percentage: float = 70, action: str = None) -> bool:
        if img1 is None or img2 is None:
            return False
        res = cv2.absdiff(img1, img2)
        result = (np.count_nonzero(res) * 100) / res.size
        if action:
            logging.debug(f"{action}, check_if_images_changed: {result}")
        return result >= percentage

    def click_position(self, position_x: int, position_y: int, waitTime: float, message: str = None):
        self.sleep(waitTime)
        x, y = self.MathUtils.randomPoint(position_x, position_y)
        self.DeviceManager.device.shell(f"input tap {x} {y}")

    def random_click_on_area(self, x1: int, y1: int, x2: int, y2: int):
        position_x, position_y = self.MathUtils.random_point_in_area(
            x1, y1, x2, y2)
        self.click_position(position_x, position_y, waitTime=0)

    def random_click_on_area_get_before_and_after_images(self, x1: int, y1: int, x2: int, y2: int) -> tuple[np.ndarray, np.ndarray]:
        before_image = self.take_screenshot()
        self.random_click_on_area(x1, y1, x2, y2)
        self.sleep(3)
        after_image = self.take_screenshot()
        return before_image, after_image

    def random_click_on_area_and_check_change_retry(self, x1: int, y1: int, x2: int, y2: int, action: str = None, percentage: float = 70) -> bool:
        self.sleep(1)
        if action:
            logging.info(f"{action}")

        for _ in range(2):
            before_image, after_image = self.random_click_on_area_get_before_and_after_images(
                x1, y1, x2, y2)
            if self.check_if_images_changed(before_image, after_image, percentage, action):
                return True

        logging.error(f"{action}")
        return False

    def ensure_not_on_sleep_mode_on_lobby(self):
        logging.info(
            "Double Click on Screen to Ensure not on Sleep Mode on Lobby")
        self.random_click_on_area(894, 848, 935, 879)
        self.sleep(1)
        self.random_click_on_area(894, 848, 935, 879)
