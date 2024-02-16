import time

import psutil
import pprint as pp

current, min_freq, max_freq = psutil.cpu_freq()
n = 10
freq_list = []
for i in range(n):
    freq = psutil.cpu_freq().current
    freq_list.append(freq)
    time.sleep(0.2)
#print(f"При {n=} следующие результаты:", freq_list)
print(f"При {n=} следующие результаты:", pp.pformat(freq_list))

n = 100
freq_list = []
for i in range(n):
    freq = psutil.cpu_freq().current
    freq_list.append(freq)
    time.sleep(0.02)
print(f"При {n=} следующие результаты:", pp.pformat(freq_list))

n = 1000
freq_list = []
for i in range(n):
    freq = psutil.cpu_freq().current
    freq_list.append(freq)
    time.sleep(0.002)
print(f"При {n=} следующие результаты:", pp.pformat(freq_list))
