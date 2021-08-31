from celery.result import AsyncResult
from app import app

res = AsyncResult("a4d6ad21-2c86-4b2a-be6d-f111f646e3c2", app=app)

print(res.state)  # 'SUCCESS'
print(res.get())  # 7
