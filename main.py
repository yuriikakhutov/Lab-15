import time
import logging

# Setting up the logger
logging.basicConfig(filename='progression.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def _log_time(func):
    def __wrapper(*args, **kwargs):
        __start_time = time.time()
        logging.info(f"Started {func.__name__}")
        result = func(*args, **kwargs)
        __end_time = time.time()
        logging.info(f"Ended {func.__name__} - Duration: {__end_time - __start_time:.4f} seconds")
        return result
    return __wrapper

class _ArithmeticProgressionIterator:
    def __init__(self, start, step):
        self.__current = start
        self.__step = step

    def __iter__(self):
        return self

    def __next__(self):
        __current = self.__current
        self.__current += self.__step
        return __current

def _arithmetic_progression_generator(start, step):
    __current = start
    while True:
        yield __current
        __current += step

@_log_time
def _sum_of_first_n_elements(iterator, n):
    return sum(next(iterator) for _ in range(n))

def main():
    __start = 3
    __step = 5
    __num_elements = [100, 1000, 10000, 100000, 1000000]

    # Using iterator
    for n in __num_elements:
        iterator = _ArithmeticProgressionIterator(__start, __step)  # Reset iterator
        print(f"Sum of first {n} elements using iterator: {_sum_of_first_n_elements(iterator, n)}")

    # Using generator
    for n in __num_elements:
        generator = _arithmetic_progression_generator(__start, __step)  # Reset generator
        print(f"Sum of first {n} elements using generator: {_sum_of_first_n_elements(generator, n)}")

if __name__ == "__main__":
    main()
