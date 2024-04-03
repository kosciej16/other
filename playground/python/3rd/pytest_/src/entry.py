from arch import Arch


class Entry:
    def __init__(self):
        self.arch = Arch()

    def start(self):
        self.arch.setup()
