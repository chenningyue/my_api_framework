import requests
from common.logger import logger
class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def request(self, method, path, **kwargs):
        url = self.base_url + path
        r = self.session.request(method, url, **kwargs)
        #print(f"{method} {url} -> {r.status_code}")

        logger.info(f"{method} {url} -> {r.status_code}")

        return r
    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)
    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)
    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)
    def patch(self, path, **kwargs):
        return self.request("PATCH", path, **kwargs)
    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)