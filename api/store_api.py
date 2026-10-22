from common.base_request import BaseRequest
from config.config import PETSTORE_BASE_URL

class StoreApi:
    def __init__(self):
        self.client = BaseRequest(PETSTORE_BASE_URL)
    def get_inventory(self):
        return self.client.get("/store/inventory")
    def create_order(self,order_body):
        return self.client.post("/store/order",json=order_body)
    def get_order(self,id):
        return self.client.get(f"/store/order/{id}")
    def delete_order(self,id):
        return self.client.delete(f"/store/order/{id}")