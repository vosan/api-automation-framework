import logging

import requests
from typing import Any, Dict, Optional
from config.settings import BASE_URL


class BaseClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = 10  # Default timeout in seconds

    def _request(
            self,
            method: str,
            endpoint: str,
            params: Optional[Dict[str, Any]] = None,
            data: Optional[Dict[str, Any]] = None,
            json: Optional[Dict[str, Any]] = None,
            **kwargs: Any
    ) -> requests.Response:
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

        response = self.session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            json=json,
            timeout=kwargs.get("timeout", self.timeout),
            **kwargs
        )
        response.raise_for_status()
        return response

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> requests.Response:
        return self._request("GET", endpoint, params=params, **kwargs)
