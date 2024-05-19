import time
from numba import njit
import matplotlib.pyplot as plt

# Ren Python Fibonacci-funktion
def fib_py(n):
    if n <= 1:
        return n
    else:
        return fib_py(n-1) + fib_py(n-2)

# Numba-accelererad Fibonacci-funktion
@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n-1) + fib_numba(n-2)

# Tidtagning och plottning
def plot_times():
    n_values = range(20, 31)
    times_py = []
    times_numba = []

    for n in n_values:
        print(n)
        # Tidtagning för ren Python
        start_time = time.perf_counter()
        fib_py(n)
        end_time = time.perf_counter()
        times_py.append(end_time - start_time)

        # Tidtagning för Numba
        start_time = time.perf_counter()
        fib_numba(n)
        end_time = time.perf_counter()
        times_numba.append(end_time - start_time)

    plt.figure()
    plt.plot(n_values, times_py, label='Python')
    plt.plot(n_values, times_numba, label='Numba')
    plt.xlabel('n')
    plt.ylabel('Tid (sekunder)')
    plt.legend()
    plt.title('Tidtagning för Fibonacci-beräkningar (n = 20, ..., 30)')
    plt.savefig('fib_times_20_30.png')
    plt.close()

plot_times()