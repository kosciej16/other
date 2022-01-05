from time import sleep
from app import A, B, BaseClass, add, app


res = A().f(1)
print(res.get())
res = B().f(1)
print(res.get())

print("END")
