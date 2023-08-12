import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")
print(fx(12))
print("done for 12")
print(fx(5))
print("done for 5")


print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")
print(fx(12))
print("done for 12")
print(fx(5))
print("done for 5")