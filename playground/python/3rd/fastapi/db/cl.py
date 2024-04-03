# import grequests
import requests as grequests


url = "http://localhost:9000"
data = {"num": 10}
data = 20

# resp1 = grequests.post(f"{url}/simple/", json=data)
# resp2 = grequests.post(f"{url}/simple/", json=10)
de = grequests.delete(f"{url}/simple/")
# res = grequests.map([resp1, resp2])
# res = grequests.map([de, resp1])
# res = grequests.map([de])
# for r in res:
#     print(r.content)
# resp = requests.get(f"{url}/simple/1")
