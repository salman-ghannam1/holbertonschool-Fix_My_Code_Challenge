#!/usr/bin/python3
"""
User Model
"""
import hashlib
import uuid


class User:
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in MD5
    """

    __password = None

    def __init__(self):
        """Create a new user"""
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        """Password getter"""
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter
        """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(
                pwd.encode()
            ).hexdigest()

    def is_valid_password(self, pwd):
        """
        Validate password
        """
        if pwd is None or type(pwd) is not str:
            return False

        if self.__password is None:
            return False

        return (
            hashlib.md5(pwd.encode()).hexdigest()
            == self.__password
        )


if __name__ == "__main__":
    print("Test User")

    user_1 = User()
    user_2 = User()

    print(user_1.id)
    print(user_2.id)

    user_1.password = "myPassword"

    print(user_1.is_valid_password("myPassword"))
    print(user_1.is_valid_password("wrongPassword"))
