import multiprocessing as mp
from time import time, sleep

def f(n:int=12) -> None:
    sleep(n)
start = time()
for i in range(1, 1000001):
    i**2
print(f"Script work time is {time() - start} s.") 
