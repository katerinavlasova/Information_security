from tree import Node
import struct
import sys

class Huffman():
    
    def __init__(self, filename):
        self.table = self.make_frequency_table(filename)
        self.codes_table = self.make_codes_table()

    def make_frequency_table(self, filename):
        table = [0] * 256
        with open(filename, "rb") as f:
            while True:
                s = f.read(1024)
                if not len(s):
                    break
                else:
                    for item in s:
                        table[item] += 1
        return table                    

    def make_codes_table(self):

        nodes = []
        for i in range(len(self.table)):
            if self.table[i] > 0:
                nodes.append(Node(i, self.table[i]))

        leafs = [] 
        codes = []
    

        if len(nodes) == 1:
            leafs.append(nodes[0])
            codes.append((nodes[0].value, "0"))
            return codes

        while len(nodes) > 1:
            nodes.sort(key=Node.sort_by_freq) 
            left, right = nodes.pop(0), nodes.pop(0)   
            new_node = Node(None, left.freq + right.freq, None, left, right) 
            left.parent = new_node 
            right.parent = new_node

            if(left.value != None):
                leafs.append(left)

            if(right.value != None):
                leafs.append(right)

            nodes.append(new_node)
        
        for leaf in leafs:
            code = ""
            node =  leaf
            while True:
                parent = node.parent
                if parent == None:
                    break
                if node == parent.left:
                    code += "0"
                if node == parent.right:
                    code += "1"
                node = parent
            codes.append((leaf.value, code[::-1]))
        #print(codes)
        return codes

    def bit_str_to_byte(self, s):
        return struct.pack('B', int(s, 2)) 

    def find_code(self, num):
        for i in range(len(self.codes_table)):
            if self.codes_table[i][0] == num:
                return self.codes_table[i][1]

        raise "Incorrect code table!"

    def find_byte(self, code):
        for i in range(len(self.codes_table)):
            if self.codes_table[i][1] == code:
                return self.codes_table[i][0]

        return None    

    # ???????????? ??????????
    def compress(self, filename):
                
        zeroes = 0
        res_filename = "compressed_" + filename
        with open(filename, "rb")  as f, open(res_filename, "wb") as res_f:
            code_str = ""
            while True:
                s = f.read(1024)
                if not len(s):
                    break
                else:
                    for item in s:
                        code = self.find_code(item)
                        code_str += code
                        if len(code_str) >= 8:
                            byte_str = code_str[:8]
                            code_str = code_str[8:]
                            byte = self.bit_str_to_byte(byte_str)
                            res_f.write(byte)

            if len(code_str) > 0:
                zeroes = 8 - len(code_str)
                for i in range(zeroes):
                    code_str += '0'
                byte = self.bit_str_to_byte(code_str)
                res_f.write(byte)

        return res_filename, zeroes


    # ???????????????????????????? ???????????????? ????????
    def decompress(self, filename, compressed_filename, zeroes):
        res_filename = "decompressed_" + filename
        with open(compressed_filename, "rb") as f, open(res_filename, "wb") as res_f:
            code_str = ""
            while True:
                s = f.read(1024)
                if not len(s):
                    break
                else:
                    for byte in s:
                        code = bin(byte)[2:].zfill(8)
                        code_str += code

            if zeroes:
                code_str = code_str[:-zeroes]

            code = ""
            while len(code_str):
                code += code_str[0]
                code_str = code_str[1:]
                byte = self.find_byte(code)
                if byte != None:
                    res_f.write(struct.pack('B', byte))
                    code = ""
      
        return res_filename
