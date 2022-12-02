from functools import wraps
from time import time_ns


def aoctimer(func):
    @wraps(func)
    def _timeit(*args, **kwargs):
        start = time_ns()
        try:
            return func(*args, **kwargs)
        finally:
            end = time_ns()
            print(f"Total time: {(end - start)/(10 ** 6)}ms")

    return _timeit
