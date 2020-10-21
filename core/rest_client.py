# -*- coding: utf-8 -*-
# @Pjname ;ApiPyTestinG
# @Time   :2020/10/22/00:27
# @Author :Yuye
# @File   :rest_client.py

import requests
import json as complexjson

class RestClient:
    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.requests(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.requests(url, "POST", data, json, **kwargs)

    def put(self, url, data, **kwargs):
        return self.requests(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.requests(url, "DELETE", **kwargs)

    def patch(self, uel, data=None, **kwargs):
        return requests(uel, "PATCH", data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return requests.post(url, data, json, **kwargs)
        if method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjsom.dumps(json)

            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)

