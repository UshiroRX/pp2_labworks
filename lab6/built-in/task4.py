from time import sleep
from math import sqrt
x = int(input())
time = int(input())

def sqrtt(x, time):
    sleep(time//1000)
    print(f"Square root of {x} after {time} miliseconds is {sqrt(x)}")

sqrtt(x, time)