import logging
from httpx import Client, HTTPError, ConnectError, ProxyError

from tenacity import retry, Retrying, stop_after_attempt, wait_fixed, RetryError


# @retry(stop=stop_after_attempt(3), wait=wait_fixed(0.2))
def get():
    http_cl = Client()
    return http_cl.post("http://www.google.com")
    # for attempt in Retrying(stop=stop_after_attempt(3), wait=wait_fixed(0.2)):
    #     with attempt:
    #         return http_cl.get("https://nonexistestdomainabc.com")


resp = get()
try:
    resp = get()
    resp.raise_for_status()
    print(resp)
except HTTPError as e:
    logging.warning(f"Warning {e}")

# print("X")
