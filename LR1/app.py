from user_hashing import UserHashing
import os

class Validator:
    def __init__(self):
        self.user_hashing = UserHashing()

    def check_validation(self):
        try:
            key_from_file = self.read_key_file()
            print(key_from_file)
        except FileNotFoundError:
            print("keyfile is not found")
            return False

        user_hash = self.user_hashing.get_user_hash()
        if user_hash == key_from_file:
            return True
        else:
            print("your key is not valid")
            return False

    @staticmethod
    def read_key_file():
        try:
            key_file = open('prog.key', 'r')
            return key_file.read()
        except FileNotFoundError:
            raise FileNotFoundError


def main():
    print("Program is working")


if __name__ == '__main__':
    validator = Validator()
    #print(os.getcwd())
    if validator.check_validation():
        print("facecontrol - OK")
        main()
    else:
        print("facecontrol - NOT OK")
    input("Enter to close")
