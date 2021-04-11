from user_hashing import UserHashing

class ProductRegister:
    def __init__(self):
        self.user_hashing = UserHashing()

    @staticmethod
    def create_key_file(info):
        key_file = open('prog.key', 'w+')
        key_file.write(info)

    def register(self):
        user_hash = self.user_hashing.get_user_hash()
        self.create_key_file(user_hash)


if __name__ == '__main__':
    productRegister = ProductRegister()
    productRegister.register()
    print('Key was successful created')
    input("Enter to close")

