import requests
from Config.config import TestData
from Methods.BaseMethods import Base_Methods

base_url = TestData.BASE_URL
api_access_token = TestData.API_ACCESS_TOKEN

class Api_Methods(Base_Methods):
        
    # POST method to create a user
    def create_user(self):
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + api_access_token}
        body = '{"name":"Apipy %s", "gender":"male","email":"%s@apipy.com", "status":"active"}' % (self.get_random_string(), self.get_random_string())
        r = requests.post(base_url + 'users/', headers = headers, data = body)
        user_id = r.json()['data']['id']
        return str(user_id)

    # PUT method to update an existing user
    def update_user(self, user_id):
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + api_access_token}
        body = '{"name":"Apipy %s", "gender":"male","email":"%s@apipy.com", "status":"active"}' % (self.get_random_string(), self.get_random_string())
        r = requests.put(base_url + 'users/' + user_id, headers = headers, data = body)
        return r.status_code

    # DELETE method to delete an existing user
    def delete_user(self, user_id):
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + api_access_token}
        r = requests.delete(base_url + 'users/' + user_id, headers = headers)
        return r.status_code
