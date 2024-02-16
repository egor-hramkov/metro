from lab2 import do_10_series, do_100_series, do_1000_series
import numpy as np

if __name__ == '__main__':
    freq_10_list = do_10_series()
    mean_10 = np.mean(freq_10_list)
    std_10 = np.std(freq_10_list)
    freq_100_list = do_100_series()
    mean_100 = np.mean(freq_100_list)
    std_100 = np.std(freq_100_list)
    freq_1000_list = do_1000_series()
    mean_1000 = np.mean(freq_1000_list)
    std_1000 = np.std(freq_1000_list)
    print(f"Для серии N={len(freq_10_list)}: Мат. ожидание = {mean_10}, Среднеквадратичное отклонение = {std_10}")
    print(f"Для серии N={len(freq_100_list)}: Мат. ожидание = {mean_100}, Среднеквадратичное отклонение = {std_100}")
    print(f"Для серии N={len(freq_1000_list)}: Мат. ожидание = {mean_1000}, Среднеквадратичное отклонение = {std_1000}")



