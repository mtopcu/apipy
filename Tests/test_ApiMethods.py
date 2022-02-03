from Methods.ApiMethods import Api_Methods
from assertpy import assert_that

class Test_Api_Methods():
    
    def test_create_user(self):
        self.apiMethods = Api_Methods()
        user_id = self.apiMethods.create_user()
        assert_that(user_id).is_not_empty()

    
    def test_create_user_and_update(self):
        self.apiMethods = Api_Methods()
        user_id = self.apiMethods.create_user()
        res = self.apiMethods.update_user(user_id)
        assert_that(res).is_equal_to(200)
    
    
    def test_create_user_and_delete(self):
        self.apiMethods = Api_Methods()
        user_id = self.apiMethods.create_user()
        res = self.apiMethods.delete_user(user_id)
        assert_that(res).is_equal_to(204)