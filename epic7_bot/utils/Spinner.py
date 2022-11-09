class Spinner(object):

    def __init__(self):
        self.frames = u'|/-\\'
        self.length = len(self.frames)
        self.position = 0

    def current(self):
        return self.frames[self.position]

    def next(self):
        current_frame = self.current()
        self.position = (self.position + 1) % self.length
        return str(current_frame)

    def reset(self):
        self.position = 0
