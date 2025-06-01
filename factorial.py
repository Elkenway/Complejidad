import time
import sys


sys.setrecursionlimit(100000)

n = 20000

def factorial_r(n):
    if n==1:
        return 1
    return n * factorial_r(n-1)


def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta