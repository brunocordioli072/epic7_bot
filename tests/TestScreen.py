import base64
import cv2
import math
import numpy as np
from epic7_bot.core.DeviceManager import DeviceManager
from epic7_bot.core.ScreenManager import ScreenManager
from epic7_bot.templates.SecretShopTemplates import SecretShopTemplates


class TestScreen:
    def __init__(self):
        self.DeviceManager = DeviceManager()
        self.ScreenManager = ScreenManager()
        self.SecretShopTemplates = SecretShopTemplates()
        self.device = None
        self.image = None
        self.filename = "test.png"
        self.coords = []

    def take_screnshot_from_area(self, x1=None, x2=None, y1=None, y2=None):
        # png_screenshot_data = device.shell("screencap -p | busybox base64")
        # png_screenshot_data = base64.b64decode(png_screenshot_data)
        # nparr = np.frombuffer(png_screenshot_data, np.uint8)
        # img = cv2.imdecode(nparr, 0)
        img = cv2.imread(self.filename)
        if x1 != None and y1 != None and x2 != None and y2 != None:
            img = img[y1:y2, x1:x2]

        return img

    def get_mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.drawMarker(self.image, (int(x), int(y)), color=(0, 255, 0))
            self.coords.append(x)
            self.coords.append(y)
            if len(self.coords) > 2:
                img = self.take_screnshot_from_area(
                    x1=self.coords[0], y1=self.coords[1], x2=self.coords[2], y2=self.coords[3])
                cv2.imwrite("test-cut.png", img)
                print(
                    f"x1={self.coords[0]}, y1={self.coords[1]}, x2={self.coords[2]}, y2={self.coords[3]}")

    def take_screnshot(self):
        png_screenshot_data = self.DeviceManager.device.shell(
            "screencap -p | busybox base64")
        png_screenshot_data = base64.b64decode(png_screenshot_data)
        with open(self.filename, "wb") as fp:
            fp.write(png_screenshot_data)

    def main(self):
        self.take_screnshot()
        cv2.namedWindow('image')
        cv2.setMouseCallback("image", self.get_mouse)

        self.image = cv2.imread(self.filename)
        while (1):
            cv2.imshow('image', self.image)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()

    def test_match(self):
        img_rgb = self.ScreenManager.take_screenshot()
        template = self.SecretShopTemplates.covenant["image"]
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where(res >= threshold)
        # pt = loc[0]
        # # print(f"x={xCoords[0]}, y={yCoords[0]}")
        pt = (loc[::-1][0][0], loc[::-1][1][0])

        # x1 = loc[::-1][0][0] + math.floor(w / 2) + 580
        # y1 = loc[::-1][1][0] + math.floor(h / 2) + 10
        # x2 = loc[::-1][0][0] + math.floor(w / 2) + 800
        # y2 = loc[::-1][1][0] + math.floor(h / 2) + 55
        # print((x1, y1), (x2, y2))
        # cv2.rectangle(img_rgb, (x1, y1), (x2, y2), (0, 0, 255), 2)

        for pt in zip(*loc[::-1]):
            print(pt)
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        while (1):
            cv2.imshow('image', img_rgb)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()


if __name__ == "__main__":
    testScreen = TestScreen()
    # testScreen.test_match()
    testScreen.main()
