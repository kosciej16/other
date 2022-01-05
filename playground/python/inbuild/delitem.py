class A:
    def __del__(self):
        print("DELETED")


a = A()


d = {1: a}
print(d)
del a
print(d)
print(d)
print(d)
