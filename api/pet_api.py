from common.base_request import BaseRequest
from config.config import PETSTORE_BASE_URL

class PetApi:
    def __init__(self):
        self.client = BaseRequest(PETSTORE_BASE_URL)
    def find_by_status(self,status):
        return self.client.get("/pet/findByStatus",params={'status':status})
    def create_pet(self,pet_body):
        return self.client.post("/pet",json=pet_body)
    def find_by_id(self,pet_id):
        return self.client.get(f"/pet/{pet_id}")
    def update_pet(self,pet_body):
        return self.client.put("/pet",json=pet_body)
    def delete_pet(self,pet_id):
        return self.client.delete(f"/pet/{pet_id}")