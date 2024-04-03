import json
import logging
from dataclasses import field, dataclass
from typing import Any, Dict
from urllib.parse import urljoin
from uuid import UUID

from requests import ConnectionError, HTTPError, Timeout, request
from tenacity import retry, stop, wait
from tenacity.retry import retry_if_exception_type

logger = logging.getLogger(__name__)


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)


@dataclass
class Client:
    base_url: str
    default_headers: Dict = field(default_factory=dict)
    timeout: int = 2
    retry_exceptions: tuple = (ConnectionError, Timeout)
    retry_attempts: int = 3
    retry_wait: Any = wait.wait_fixed(0.1)

    @retry(
        retry=retry_if_exception_type(retry_exceptions),
        stop=stop.stop_after_attempt(retry_attempts),
        wait=retry_wait,
        reraise=True,
    )
    def request(self, path, **kwargs):
        kwargs["url"] = urljoin(self.base_url, path)
        kwargs["headers"] = {
            "Accept": "application/json",
            **self.default_headers,
            **kwargs.get("headers", {}),
        }
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout

        logger.info("[%s] request: %s", self.__class__.__name__, kwargs["url"])
        logger.debug("[%s] request params: %s", self.__class__.__name__, kwargs)
        response = request(**kwargs)
        logger.debug("[%s] response: %s", self.__class__.__name__, response.content)

        if response.status_code == 400:
            raise HTTPError(
                f"400 HTTP Error [{response.url}]: {response.content}",
                response=response,
            )
        response.raise_for_status()

        return response

    def get(self, path, json_data="", **kwargs):
        return self.request(
            path, method="GET", data=json.dumps(json_data, cls=UUIDEncoder), **kwargs
        )

    def post(self, path, json_data="", **kwargs):
        return self.request(
            path, method="POST", data=json.dumps(json_data, cls=UUIDEncoder), **kwargs
        )

    def put(self, path, json_data, **kwargs):
        return self.request(
            path, method="PUT", data=json.dumps(json_data, cls=UUIDEncoder), **kwargs
        )

    def patch(self, path, json_data="", **kwargs):
        return self.request(
            path, method="PATCH", data=json.dumps(json_data, cls=UUIDEncoder), **kwargs
        )
