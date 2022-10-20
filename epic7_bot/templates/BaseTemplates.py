import os


class BaseTemplates(object):
    def __init__(self):
        self.dirPath = os.path.dirname(os.path.abspath(__file__))
