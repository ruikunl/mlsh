import numpy as np
import matplotlib.pyplot as plt

import pickle
import IPython
if __name__== '__main__':
    dir = "./"
    total_data = []
    mean_data = []
    std_data = []
    for ind in range(506):
        file_name = dir + "outfile"+ str(ind)+".pickle"
        fs = open(file_name, 'rb')
        data = pickle.load(fs)
        total_data.append(data)
        mean_data.append(np.mean(data))
        std_data.append(np.std(data))

    plt.plot(mean_data)
    plt.show()
