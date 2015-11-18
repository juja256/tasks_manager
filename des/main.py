from des import *

if __name__ == "__main__":
    file1 = open("sonets.txt", "r").read()
    d = DES(key='helloam', data=file1).encrypt()
    print d.tobytes()
    a = DES(key='helloam', data=d).decrypt()
    print a.tobytes()
