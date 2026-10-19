
from common.base_request import BaseRequest
from config.config import HTTPBIN_BASE_URL

class BearerApi:
    def __init__(self):
        self.client = BaseRequest(HTTPBIN_BASE_URL)
    def bearer(self,token = None):
        headers={'Authorization': f'Bearer {token}'} if token else {}
        return self.client.get("/bearer",headers=headers)