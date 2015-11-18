from tasks import *
from des import *


def factorial(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return n

def des_encryption(key, msg):
    return DES(key=key, data=msg).encrypt()

def des_test():
    return DES(key=b"helloim", data=b"Hello World").encrypt()

tm = TaskManager(3)
t1 = tm.add_task(des_encryption, b"helloik", b"Hello")
t2 = tm.add_task(des_test)
t3 = tm.add_task(des_encryption, b"helloio", b"Hello")
t4 = tm.add_task(des_encryption, b"helloiv", b"Hello")
c1 = tm.force_get_result(t1)
c2 = tm.force_get_result(t2)
c3 = tm.attempt_get_result(t3)
c4 = tm.attempt_get_result(t4)
print(c1)
print(c2)
print(c3)
print(c4)