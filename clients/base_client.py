"""
Base API client implementation.
"""
from utils import logger
import requests
from typing import Any, Dict, Optional
from config.settings import BASE_URL


class BaseClient:
    """
    A foundational API client to handle HTTP session management, logging, and common request logic.
    """
    def __init__(self, base_url: str = BASE_URL):
        """
        Initializes the client with a base URL and a shared requests Session.
        """
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
        """
        Internal method to execute HTTP requests with logging and error handling.
        """
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        logger.info(f"Sending {method} request to: {url}")

        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json,
                timeout=kwargs.get("timeout", self.timeout),
                **kwargs
            )
            logger.info(f"Received response with status code: {response.status_code}")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> requests.Response:
        """
        Executes a GET request.
        """
        return self._request("GET", endpoint, params=params, **kwargs)
