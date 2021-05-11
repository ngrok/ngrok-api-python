from __future__ import annotations
from collections.abc import Iterator
from typing import Any, Mapping, Dict, Generic, Optional
import os
import requests

from .error import Error, NotFoundError


class APIClient(object):
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def get(self, path: str, params: Mapping[str, str]) -> Dict[str, Any]:
        return self.jsonDo("get", path, query_params=params)

    def post(self, path: str, data: Mapping[str, Any]) -> Dict[str, Any]:
        return self.jsonDo("post", path, payload=data)

    def put(self, path: str, data: Mapping[str, Any]):
        return self.jsonDo("put", path, payload=data)

    def patch(self, path: str, data: Mapping[str, Any]):
        return self.jsonDo("patch", path, payload=data)

    def delete(self, path, data: Mapping[str, Any]) -> None:
        self.do("delete", path, payload=data)

    def jsonDo(
        self,
        method: str,
        path: str,
        query_params: Mapping[str, str] = None,
        payload: Mapping[str, Any] = None,
    ) -> Dict[str, Any]:
        """like do, but expects a return value"""
        resp = self.do(method, path, query_params, payload)
        if resp is None:
            raise RuntimeError("server returned unexpected 204 response")
        return resp

    def do(
        self,
        method: str,
        path: str,
        query_params: Mapping[str, str] = None,
        payload: Mapping[str, Any] = None,
    ) -> Optional[Dict[str, Any]]:
        url = self.base_url + path
        resp = requests.request(
            method,
            url,
            params={k: v for k, v in query_params.items() if v}
            if query_params
            else None,
            headers={
                "ngrok-version": "2",
                "authorization": "Bearer " + self.api_key,
            },
            json={k: v for k, v in payload.items() if v is not None}
            if payload
            else None,
        )
        if not resp.ok:
            self._throw_error(resp)
            return None
        elif resp.status_code == 204:
            return None
        else:
            return resp.json()

    def request(self, method: str, url: str) -> Dict[str, Any]:
        """makes an authenticated request to a URL
        this is used for paging where we already have a full url and don't need to construct one
        """
        resp = requests.request(
            method,
            url,
            headers={
                "ngrok-version": "2",
                "authorization": "Bearer " + self.api_key,
            },
        )
        if not resp.ok:
            self._throw_error(resp)
        return resp.json()

    def _throw_error(self, resp: requests.Response) -> None:
        if resp.status_code >= 500:
            raise RuntimeError(
                "Server failed with {} and body '{}'".format(
                    resp.status_code, resp.text
                )
            )

        try:
            err = resp.json()
        except:
            raise RuntimeError(
                "Server failed with {} and body '{}'".format(
                    resp.status_code, resp.text
                )
            )

        if resp.status_code == 404:
            raise NotFoundError(
                error_code=err.get("error_code"),
                http_status_code=err["status_code"],
                message=err["msg"],
                details=err["details"],
            )
        else:
            raise Error(
                error_code=err.get("error_code"),
                http_status_code=err["status_code"],
                message=err["msg"],
                details=err["details"],
            )
