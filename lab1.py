import psutil

current, min_freq, max_freq = psutil.cpu_freq()
print(f"Частота процессора: \nТекущая: {current} \nМинимальная: {min_freq} \nМаксимальная: {max_freq}")
