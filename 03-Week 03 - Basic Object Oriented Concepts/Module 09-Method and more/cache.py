# 0, 1, 1, 2, 3, 5, 8, 13----

import time
from functools import cache

@cache
def fib(n):

    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)

start = time.time()

for i in range(1,10):
    print(i, fib(i))

end = time.time()

print("Total time : ",(end-start)*1000)

# 3.393411636352539