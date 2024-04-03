from runner import Runner


class Arch:
    def __init__(self):
        self.runner = None

    def setup(self):
        self.runner = Runner()
        self.runner.start()
