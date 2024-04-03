import requests
from requests.adapters import HTTPAdapter, Retry

from app import AllSModel, Inter, StatesModel


data = {
    "AllSeries": {
        "s1": {"s_id": 1, "s_name": "Apple"},
        "s2": {"s_id": 2, "s_name": "Basket"},
        "s3": {"s_id": 3, "s_name": "Commerce"},
    }
}
url = "http://localhost:5959/so"
# data = {"a": "b"}

# resp = requests.get(url, data=data)
session = requests.Session()
# session.mount(
#     "http://",
#     HTTPAdapter(
#         max_retries=Retry(
#             total=5,
#             backoff_factor=1,
#             status_forcelist=[429, 500, 502, 503, 504],
#             respect_retry_after_header=False,
#         )
#     ),
# )

resp = session.post(url, json=data)
x = resp.json()
print(x)
print(StatesModel.parse_obj(x))
