import math
from random import random as rand
import random


from epic7_bot.utils.Singleton import Singleton


class MathUtils(metaclass=Singleton):
    def randomPoint(self, aroundX, aroundY, scale=1, density=2):
        angle = rand()*2*math.pi

        x = rand()
        if x == 0:
            x = 0.0000001

        distance = scale * (pow(x, -1.0/density) - 1)
        return (aroundX + distance * math.sin(angle),
                aroundY + distance * math.cos(angle))

    def midpoint(self, x1, y1, x2, y2):
        return ((x1 + x2)/2, (y1 + y2)/2)

    def random_point_in_area(self, x1, y1, x2, y2):
        x = random.uniform(x1, x2)
        y = random.uniform(y1, y2)
        return x, y
