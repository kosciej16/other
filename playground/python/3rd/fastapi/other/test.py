def foo():
    print("A")

class Justyna:
    # wiek = 10

    def __init__(self, wiek):
        self.wiek = wiek

    def graj(self):
        print(f"JUSTYNA GRA I MA {self.wiek} lat")


mloda = Justyna(20)
print(mloda.wiek)
mloda.graj()
# stara = Justyna(25)
# print(stara.wiek)
# a.graj()
