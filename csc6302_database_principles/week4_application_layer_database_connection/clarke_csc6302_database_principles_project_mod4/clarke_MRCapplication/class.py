
from typing import List, Dict
class User:
    # global dict to hold users
    db: Dict = {}
    def __init__(self, name: str, age: int, height: str):
        self.name = name
        self.age=age
        self.height = height
        self.add_users(name, age, height)
        
    
    # this method adds users to list
    def add_users(self, name: str, age: int, height: str):
        # adding user to db
        User.db[self.name]={"age": self.age, "height": self.height}

    # This method retrieves the user's name
    def get_username(self) -> str:
        print(f"Username is: {User.db[self.name]}")

    def get_age(self) -> int:
        print(f"Username is: {self.age}")
    
    def get_height(self) -> str:
        print(f"Username is: {self.height}")

    def disp_all_users(self):
        for key, value in User.db.items():
            print(f"{key}: {value}")

    

jay = User("jay", 32, "6'")

jay.disp_all_users()
jay.get_age()




    