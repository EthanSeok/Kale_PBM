import numpy as np
import matplotlib.pyplot as plt


def main():
    optTemp = 15.7
    optVer = 6.2
    Ta = np.linspace(0, 30, 300)
    Ta = np.maximum(Ta, 0.01)
    temp_rate = np.exp(- 1 *(np.log(Ta/optTemp )**2))
    ver_rate = np.exp(-1 * (np.log(Ta / optVer) ** 4))
    tot_rate = temp_rate * ver_rate

    plt.plot(Ta, temp_rate, color='blue', label='temp_rate')
    plt.plot(Ta, ver_rate, color='orange', label='ver_rate')
    plt.plot(Ta, tot_rate, color='green', label='DVS')
    plt.xlabel('temp(°C)')
    plt.ylabel('rate')
    plt.title('DVS fraction')
    plt.legend()
    plt.savefig('./graph/dvs_fraction.png')
    plt.show()

if __name__ == "__main__":
    main()
