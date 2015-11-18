from perm import *
from utils import *


class DES:
    __ip = (58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7)

    __p5 = (57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4)

    __p7 = (14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32)

    __shift_table = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)

    __e = (32, 1, 2, 3, 4, 5,
           4, 5, 6, 7, 8, 9,
           8, 9, 10, 11, 12, 13,
           12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21,
           20, 21, 22, 23, 24, 25,
           24, 25, 26, 27, 28, 29,
           28, 29, 30, 31, 32, 1)

    __s = (((14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
            (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
            (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
            (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13)),

           ((15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10),
            (3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5),
            (0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15),
            (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9)),

           ((10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8),
            (13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1),
            (13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7),
            (1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12)),

           ((7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15),
            (13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9),
            (10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4),
            (3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14)),

           ((2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9),
            (14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6),
            (4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14),
            (11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3)),

           ((12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11),
            (10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8),
            (9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6),
            (4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13)),

           ((4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1),
            (13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6),
            (1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2),
            (6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12)),

           ((13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7),
            (1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2),
            (7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8),
            (2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11)))

    __p = (16, 7, 20, 21, 29, 12, 28, 17,
           1, 15, 23, 26, 5, 18, 31, 10,
           2, 8, 24, 14, 32, 27, 3, 9,
           19, 13, 30, 6, 22, 11, 4, 25)

    def __feistel_iteration(self, iteration, block):
        L = block[:32]
        R = block[32:]
        R1 = self.__feistel_function(R, self.__session_keys_pack[iteration])
        R1 ^= L
        return R1 + R

    def __feistel_function(self, block, session_key48):
        extended = self.__E.Reduce(block, 48)
        xored = extended ^ session_key48
        block32 = bitarray()
        for i in range(0, 8):
            b6 = xored[i * 6:(i + 1) * 6]
            a = bitarray([b6[0], b6[5]])
            b = b6[1:5]
            aint = BitUtils.bitarray_to_int(a)
            bint = BitUtils.bitarray_to_int(b)
            b4 = BitUtils.int_to_bitarray(self.__s[i][aint][bint], 4)
            block32 += b4

        return self.__P.Substitude(block32)



    def __key_transform64(self):
        tran = bitarray(64 * [0])
        for i in range(0, 8):
            b7 = self.__key[i * 7: (i + 1) * 7]
            tran[i * 8: (i + 1) * 8 - 1] = b7
            tran[(i + 1) * 8 - 1] = 1 if b7.count(1) % 2 == 0 else 0

        self.__key = tran

    def __generate_session_keys_pack(self):
        cd = self.__P5.Reduce(self.__key, 56)

        for i in range(0, 16):
            c = BitUtils.lshift(cd[:28], self.__shift_table[i])
            d = BitUtils.lshift(cd[28:], self.__shift_table[i])
            cd = c + d
            self.__session_keys_pack.append(self.__P7.Reduce(cd, 48))

    def __init__(self, **kwargs):
        self.__msg = None
        self.__key = bitarray()  # initial 64 bit key
        self.__enc = bitarray()
        self.__key_raw = None
        self.__msg_raw = None
        self.__session_keys_pack = []

        if 'key' in kwargs:
            self.set_key(kwargs['key'])

        if 'data' in kwargs:
            self.set_data(kwargs['data'])

        self.__P5 = Permutation(self.__p5)
        self.__P7 = Permutation(self.__p7)
        self.__E = Permutation(self.__e)
        self.__P = Permutation(self.__p)
        self.__IP = Permutation(self.__ip)

    def set_data(self, data):
        if type(data) == str:
            self.__msg = bitarray()
            self.__msg.frombytes(data)
            self.__msg_raw = data
        elif type(data) == bitarray:
            self.__msg_raw = data
            self.__msg = data

    def set_key(self, key):
        if type(key) == bitarray:
            if key.length() != 56:
                raise ValueError("Key is not valid")
            self.__key = key
            self.__key_transform64()
            self.__key_raw = key
        elif type(key) == str:  # 7 bytes max!!!
            self.__key.frombytes(key)
            self.__key_raw = self.__key.copy()
            self.__key_transform64()

    def get_key_64_bin(self):
        return ' '.join([self.__key[i:i + 8].to01() for i in range(0, len(self.__key), 8)])

    def encrypt(self, **kwargs):
        if 'key' in kwargs:
            self.set_key(kwargs['keys'])

        if 'data' in kwargs:
            self.set_data(kwargs['data'])

        #print "Encryption begins...\nKey64: " + BitUtils.bitarray_fancy_view(self.__key)
        #print "Data: " + BitUtils.bitarray_fancy_view(self.__msg)

        self.__generate_session_keys_pack()
        adj = (64 - self.__msg.length() % 64) if self.__msg.length() % 64 != 0 else 0
        self.__msg = self.__msg + (bitarray('0') * adj)  # adjust data to 64 bit blocks
        bare = self.__IP.Substitude(self.__msg)

        for i in range(0, bare.length() / 64):
            block = bare[i * 64:(i + 1) * 64]

            for j in range(0, 16):
                block = self.__feistel_iteration(j, block)

                if j != 15:
                    block = BitUtils.swap_block64(block)  # in last iteration we don't need swapping
                #print "block #" + str(i) + "; iteration #" + str(j) + ": " + BitUtils.bitarray_fancy_view(block)

            self.__enc += block
        self.__enc = self.__IP.Reverse().Substitude(self.__enc)
        #print "Encrypted: " + BitUtils.bitarray_fancy_view(self.__enc)
        return self.__enc

    def decrypt(self, **kwargs):
        if 'key' in kwargs:
            self.set_key(kwargs['keys'])

        if 'data' in kwargs:
            self.set_data(kwargs['data'])

        if self.__msg.length() % 64 != 0:
            raise ValueError("Ciphertext' lenght is not divided by 64.")

        #print "Decryption begins...\nKey64: " + BitUtils.bitarray_fancy_view(self.__key)
        #print "Data: " + BitUtils.bitarray_fancy_view(self.__msg)
        self.__generate_session_keys_pack()

        bare = self.__IP.Substitude(self.__msg)

        for i in range(0, bare.length() / 64):
            block = bare[i * 64:(i + 1) * 64]

            for j in reversed(range(0, 16)):
                block = self.__feistel_iteration(j, block)

                if j != 0:
                    block = BitUtils.swap_block64(block)  # in last iteration we don't need swapping
                #print "block #" + str(i) + "; iteration #" + str(j) + ": " + BitUtils.bitarray_fancy_view(block)

            self.__enc += block

        self.__enc = self.__IP.Reverse().Substitude(self.__enc)
        #print "Decrypted: " + BitUtils.bitarray_fancy_view(self.__enc)

        return self.__enc
