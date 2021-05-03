from random import randint, shuffle
import string

r1 = ['e', 'k', 'm', 'f', 'l', 'g', 'd', 'q', 'v', 'z', 'n', 't', 'o', 'w', 'y', 'h', 'x', 'u', 's', 'p', 'a', 'i', 'b',
      'r', 'c', 'j']

r2 = ['a', 'j', 'd', 'k', 's', 'i', 'r', 'u', 'x', 'b', 'l', 'h', 'w', 't', 'm', 'c', 'q', 'g', 'z', 'n', 'p', 'y', 'f',
      'v', 'o', 'e']

r3 = ['b', 'd', 'f', 'h', 'j', 'l', 'c', 'p', 'r', 't', 'x', 'v', 'z', 'n', 'y', 'e', 'i', 'w', 'g', 'a', 'k', 'm', 'u',
      's', 'q', 'o']

rflctr = ['y', 'r', 'u', 'h', 'q', 's', 'l', 'd', 'p', 'x', 'n', 'g', 'o', 'k', 'm', 'i', 'e', 'b', 'f', 'z', 'c', 'w',
          'v', 'j', 'a', 't']


class Rotor:
    def __init__(self, rotor_data, shift=None, mark=None):
        self.data = rotor_data
        self.shift = shift
        self.mark = mark

    def update_shift(self):
        self.shift = (self.shift + 1) % len(self.data)
        result = 1 if self.shift == self.mark else 0
        return result

    def encrypt_front(self, byte, tmp_shift=0):
        index = (ord(byte) % 97 + (self.shift - tmp_shift)) % len(self.data)
        encrypted = self.data[index]  
        return encrypted, self.shift

    def encrypt_back(self, byte, tmp_shift=0):
        encrypted = fix_index(ord(byte) + self.shift - tmp_shift)  # формируем байт
        encrypted_index = self.data.index(chr(encrypted))  # ищем его в списке, получаем индекс
        return chr(encrypted_index + 97), self.shift


class Reflector:
    def __init__(self, reflector):
        self.data = reflector

    def reflect(self, byte, shift):
        index = (ord(byte) % 97 - shift) % len(self.data)
        return self.data[index]


def fix_index(encrypted):
    if encrypted >= 123:
        encrypted = (encrypted % 123) + 97
    elif encrypted < 97:
        encrypted = 123 - (97 - encrypted)
    return encrypted


def update_rotor(rotor, flag):
    if flag:
        return rotor.update_shift()
    else:
        return 0
    

def encrypt(byte, reflector, rotor1, rotor2, rotor3):
    update_flag = rotor1.update_shift()
    symbol, shift = rotor1.encrypt_front(byte)

    update_flag = update_rotor(rotor2, update_flag)
    symbol, shift = rotor2.encrypt_front(symbol, shift)

    update_flag = update_rotor(rotor2, update_flag)
    symbol, shift = rotor3.encrypt_front(symbol, shift)

    symbol = reflector.reflect(symbol, shift)

    symbol, shift = rotor3.encrypt_back(symbol)
    symbol, shift = rotor2.encrypt_back(symbol, shift)
    symbol, shift = rotor1.encrypt_back(symbol, shift)
    symbol = chr(fix_index(ord(symbol) - shift))
    
    return symbol


def encrypt_name(name: str) -> str:
    name = name.lower()
    
    reflector = Reflector(rflctr)
    rotor1 = Rotor(r1, ord('q') % 97, 25)  
    rotor2 = Rotor(r2, ord('v') % 97, 25)  
    rotor3 = Rotor(r3, ord('c') % 97, 25)

    encrypted = ''

    for byte in name:
        if byte not in string.punctuation:
            encrypted += encrypt(byte, reflector, rotor1, rotor2, rotor3)
        else:
            encrypted += byte

    return encrypted
