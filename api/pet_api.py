from common.base_request import BaseRequest
from config.config import PETSTORE_BASE_URL

class PetApi:
    def __init__(self):
        self.client = BaseRequest(PETSTORE_BASE_URL)
    def find_by_status(self,status):
        return self.client.get("/pet/findByStatus",params={'status':status})
