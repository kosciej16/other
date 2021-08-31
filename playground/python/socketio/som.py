import asyncio


class MyLock:
    def __init__(self):
        self.lock = asyncio.Lock()
