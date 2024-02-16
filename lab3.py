import matplotlib.pyplot as plt
from lab2 import do_10_series, do_100_series, do_1000_series


def show_graphic_data(graph_data):
    plt.clf()
    plt.xlabel("Частота, об/мин")
    plt.title(f'Частота процессора при N={len(graph_data)}, МГц')
    plt.plot(graph_data)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    freq_10_list = do_10_series()
    show_graphic_data(freq_10_list)
    freq_100_list = do_100_series()
    show_graphic_data(freq_100_list)
    freq_1000_list = do_1000_series()
    show_graphic_data(freq_1000_list)

