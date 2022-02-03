import random, string

class Base_Methods():
    
    def get_random_string(self):
        return ''.join(random.choice(string.ascii_letters) for _ in range(6))