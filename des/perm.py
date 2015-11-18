from bitarray import *

class Permutation:

    def __init__(self, l):
        # if sorted(l) != range(1, len(l)+1):
        #	raise ValueError("List is not valid!")
        self.__bare = [i - 1 for i in l]

    def Get(self):
        return self.__bare

    def Reverse(self):
        rev = [0] * len(self.__bare)
        for i in range(0, len(self.__bare)):
            rev[self.__bare[i]] = i + 1

        return Permutation(rev)

    def Substitude(self, msg):
        """
            Substitudes all bits in input message
        """

        bits = bitarray()
        if type(msg) == str or type(msg) == bytes:
            bits.frombytes(msg)
        elif type(msg) == bitarray:
            bits = msg
        else:
            raise ValueError("Not valid type of input data")

        res = bitarray(bits.length() * [0])
        size = len(self.__bare)
        for i in range(0, bits.length()):
            res[i] = bits[(i // size) * size + self.__bare[i % size]]
        return res

    def Reduce(self, block, size):
        """
        Shrinks or extends block to specified size with permutation
        """

        bits = bitarray()
        if type(block) == str or type(block) == bytes:
            bits.frombytes(block)
        elif type(block) == bitarray:
            bits = block
        else:
            raise ValueError("Not valid type of input data")

        res = bitarray(size * [0])

        for i in range(0, size):
            res[i] = bits[self.__bare[i]]
        return res