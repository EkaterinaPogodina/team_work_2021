#Написать функцию, получающую на вход два числа
# и возвращающую их сумму
#Написать функцую, получающую на вход число и степень
# , в которую надо его возвести
#Обернуть эти две функции в декоратор, который
# печает время работы начала работы программы
# и конец работы программы
# (в человеко читаемом формате - поискать в интернете как это делается)

import time
def get_run_time(func):
    def func_wrap(num_a, num_b):
        start_time = time.time()
        func(num_a, num_b)
        end_time = time.time()
        run_time = end_time - start_time
        si_notation = ['seconds', 'milliseconds', 'microseconds', 'nanoseconds']
        for i in range(0, len(si_notation)):
            if run_time * (1000**i) >= 1:
                print(f'{round(run_time * (1000**i), 4)} {si_notation[i]}')
                break
        return func(num_a, num_b)

    return func_wrap


@get_run_time
def get_sum_of_two(num_a, num_b):
    return num_a + num_b


@get_run_time
def get_power(num_a, num_b):
     return num_a ** num_b


#get_power(3, 22)
#get_sum_of_two(6, 67)
