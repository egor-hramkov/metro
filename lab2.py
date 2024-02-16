import time

import psutil
import pprint as pp


def do_10_series():
    n = 10
    freq_list = []
    for i in range(n):
        freq = psutil.cpu_freq().current
        freq_list.append(freq)
        time.sleep(0.2)
    print(f"При {n=} следующие результаты:", pp.pformat(freq_list))
    return freq_list


def do_100_series():
    n = 100
    freq_list = []
    for i in range(n):
        freq = psutil.cpu_freq().current
        freq_list.append(freq)
        time.sleep(0.02)
    print(f"При {n=} следующие результаты:", pp.pformat(freq_list))
    return freq_list


def do_1000_series():
    n = 1000
    freq_list = []
    for i in range(n):
        freq = psutil.cpu_freq().current
        freq_list.append(freq)
        time.sleep(0.002)
    print(f"При {n=} следующие результаты:", pp.pformat(freq_list))
    return freq_list


if __name__ == "__main__":
    do_10_series()
    do_100_series()
    do_1000_series()
