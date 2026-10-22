from common.base_request import BaseRequest
from config.config import PETSTORE_BASE_URL

class UserApi:
    def __init__(self):
        self.client = BaseRequest(PETSTORE_BASE_URL)
    def create_user(self,pet_body):
        return self.client.post("/user",json=pet_body)
    def get_user(self,username):
        return self.client.get(f"/user/{username}")
    def update_user(self,username,user_body):
        return self.client.put(f"/user/{username}",json=user_body)
    def delete_user(self,username):
        return self.client.delete(f"/user/{username}")
    def login_user(self,username,password):
        return self.client.get("/user/login",params={"username":username,"password":password})