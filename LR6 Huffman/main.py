import sys
import os
from huffman import Huffman


def main():
    filename = 'ziip.rar' #'test.txt'
    print("Исходный файл: '{}' ({} байт)".format(filename, os.path.getsize(filename)))
    huf = Huffman(filename)
    res_filename, zeroes = huf.compress(filename)
    print("Сжатый файл: '{}'  ({} байт)".format(res_filename,  os.path.getsize(res_filename)))
    print("Нулей дописано в последний байт:", zeroes)

    dec_filename = huf.decompress(filename, res_filename, zeroes)
    print("Восстановленный файл: '{}'  ({} байт)".format(dec_filename,  os.path.getsize(dec_filename)))

if __name__ == '__main__':
    main()
