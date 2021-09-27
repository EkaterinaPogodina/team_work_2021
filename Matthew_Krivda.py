import time


def work_time(func):
    def time_counter(*args):
        start_counter = time.perf_counter()
        func_execution = func(*args)
        end_counter = time.perf_counter()
        print(f'Function executing time is{end_counter - start_counter : 0.3f} seconds')
        return func_execution

    return time_counter


@work_time
def num_sum(num_1, num_2):
    return num_1 + num_2


@work_time
def num_pow(base, power):
    return base ** power


n_1, n_2 = map(float, input().strip().split())
print("Sum of numbers is", num_sum(n_1, n_2))
print('First number in power of another is', num_pow(n_1, n_2))
