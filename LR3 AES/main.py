from aes128 import encrypt, decrypt
from FileNameEncryptor import encrypt_name


def write_bytes(file, bytes_list):
    for byte in bytes_list:
        file.write(bytes([byte]))


def read_bites(file):
    lst = []
    while True:
        byte = file.read(1)
        if not byte:
            break
        else:
            lst.append(int.from_bytes(byte, 'big'))

    return lst


def main():
    config_file_name = input('Input config data file name: ')
    data_file_name = input("Input data file name: ")
    encrypted_file_name = encrypt_name(data_file_name)
    decrypted_file_name = data_file_name.split('.')[0] + '_decrypted.' + data_file_name.split('.')[1]

    with open(config_file_name, 'rb') as config_file:
        key = read_bites(config_file)  # [int.from_bytes(i) for i in config_file.read().split()]
        config_file.close()
    with open(data_file_name, 'rb') as data_file:
        data = read_bites(data_file)  # data_file.read().split()
        # print("input_data = ", data)
        data_file.close()
    with open(encrypted_file_name, 'wb') as encrypted_file:
        encrypted = encrypt(data, key)
        # print("encrypted = ", encrypted)
        write_bytes(encrypted_file, encrypted)
        encrypted_file.close()
    with open(decrypted_file_name, 'wb') as decrypted_file:
        decrypted = decrypt(encrypted, key)
        # print('encrypted = ', decrypted)
        write_bytes(decrypted_file, decrypted)
        decrypted_file.close()


if __name__ == '__main__':
    main()

