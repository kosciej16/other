from time import sleep
from app import A, B, BaseClass, add, app, g

from tasks import AddTask

# from tasks import AddTask

app.send_task("app.add", kwargs={"x": 1, "y": 2})

# res = AddTask.delay([1, 2, 3])

# res = AddTask().run(1, 2)
# print(res.get())
# res = add.delay(1, 2)
# print(res)
# g.delay("10")
# res = A().f(1)
# print(res.get())
# res = B().f(1)
# print(res.get())

print("END")
