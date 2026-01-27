import timeit

cache = {}


def fib(n):
    if n <= 1:
        return n

    if n in cache:
        return cache[n]
    else:
        result = fib(n - 1) + fib(n - 2)
        cache[n] = result
        return result



# assert fib(0) == 0
# assert fib(1) == 1
# assert fib(2) == 1
# assert fib(3) == 2
# assert fib(4) == 3
# assert fib(5) == 5
# assert fib(6) == 8
# assert fib(7) == 13

start = timeit.default_timer()
assert fib(25)
elapsed = timeit.default_timer() - start

print(f"elapsed: {elapsed:.10f} s")
