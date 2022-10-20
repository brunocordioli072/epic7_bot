import math
from random import random


class MathUtils:
    def randomPoint(self, aroundX, aroundY, scale=1, density=2):
        angle = random()*2*math.pi

        x = random()
        if x == 0:
            x = 0.0000001

        distance = scale * (pow(x, -1.0/density) - 1)
        return (aroundX + distance * math.sin(angle),
                aroundY + distance * math.cos(angle))

    def midpoint(self, x1, y1, x2, y2):
        return ((x1 + x2)/2, (y1 + y2)/2)
