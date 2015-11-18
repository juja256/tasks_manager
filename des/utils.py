from bitarray import *
import struct


def bitarray_to_int(b):
    return struct.unpack("<b", b.tobytes())[0]
    #c = 0
    #for i in range(0, size):
    #    c += b[size - i - 1] * 2 ** i
    #return c


def bitarray_to_hex(b):
    return ' '.join(format(x, '02x') for x in bytearray(b.tobytes()))


def bitarray_fancy_view(b):
    return ' '.join([b[i:i + 8].to01() for i in range(0, b.length(), 8)])


def int_to_bitarray(number, size):
    a = bitarray()
    a.frombytes(struct.pack("B", number))
    return a[-size:]


def lshift(a, count):
    return a[count:] + a[0:count]


def rshift(a, count):
    return a[len(a) - count:] + a[:-count]


def swap_block64(block):
    return rshift(block, 32)
