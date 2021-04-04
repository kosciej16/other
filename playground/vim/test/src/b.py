class B:
    def __init__(self, a=10, b=20):
        self.a = a
        self.b = b

    def __call__(self):
        print("10")

    def foo(self):
        return 1
