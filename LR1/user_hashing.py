import subprocess
import hashlib

class UserHashing:

    @staticmethod
    def get_serial_number():
        result = subprocess.run("wmic bios get serialnumber", stdout=subprocess.PIPE, shell=True, check=True)
        serial_number = result.stdout.strip()
        return serial_number.decode("utf-8")

    @staticmethod
    def hash_info(*args):
        compared_info = ''
        for arg in args:
            compared_info += arg

        hash_info = hashlib.md5(compared_info.encode())
        return hash_info.hexdigest()

    def get_user_hash(self):
        serial_number = self.get_serial_number()
        return self.hash_info(serial_number)
