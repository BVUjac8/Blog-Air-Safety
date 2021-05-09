# Julia Cuellar
# DSC 640
# Blog

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math


# Will use in Blog
def read_file():
    air = pd.read_csv('air-safety.csv')
    print('Data:\n', air)
    # plt.hist(air)
    # plt.title('Histogram of Air')
    # plt.show()


def read_file2():
    plane = pd.read_csv('Airplane_Crashes_and_Fatalities_Since_1908.csv')
    print("Display data with null:\n", plane.isnull())
    print("Display counts of null from data:\n", plane.isnull().sum())
    print('Data:\n', plane)


# Will use in Blog
def read_file3():
    fin = pd.read_csv('Financial_Results__1947-Present_Full_Data_data.csv')
    print("Display data with null:\n", fin.isnull())
    print("Display counts of null from data:\n", fin.isnull().sum())
    print('Data:\n', fin)
    pax = fin['Pax (mils)']
    plt.hist(pax, color='orange')
    plt.title('Airline PAX', font='Viner Hand ITC', fontsize=15)
    plt.xlabel('PAX in millions')
    plt.legend(['PAX (mils)'])
    plt.grid()
    plt.show()


def read_file4():
    ffin = pd.read_csv('Financials_Full_Data_data.csv')
    print("Display data with null:\n", ffin.isnull())
    print("Display counts of null from data:\n", ffin.isnull().sum())
    print('Data:\n', ffin)


# Will use in Blog
def read_file5():
    traffic = pd.read_csv('Traffic_&_Capacity_Full_Data_data.csv')
    print("Display data with null:\n", traffic.isnull())
    print("Display counts of null from data:\n", traffic.isnull().sum())
    print('Data:\n', traffic)
    x = traffic['Year']
    y = traffic['Load Factor']
    grid_size = 1
    h = 10
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)
    x_grid = np.arange(x_min - h, x_max + h, grid_size)
    y_grid = np.arange(y_min - h, y_max + h, grid_size)
    x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)
    xc = x_mesh + (grid_size / 2)
    yc = y_mesh + (grid_size / 2)

    def kde_quartic(d, h):
        dn = d / h
        P = (15 / 16) * (1 - dn ** 2) ** 2

        return P

    intensity_list = []

    for j in range(len(xc)):
        intensity_row = []

        for k in range(len(xc[0])):
            kde_value_list = []

            for i in range(len(x)):
                d = math.sqrt((xc[j][k] - x[i]) ** 2 + (yc[j][k] - y[i]) ** 2)

                if d <= h:
                    p = kde_quartic(d, h)
                else:
                    p = 0
                kde_value_list.append(p)
            p_total = sum(kde_value_list)
            intensity_row.append(p_total)
        intensity_list.append(intensity_row)

    intensity = np.array(intensity_list)
    plt.pcolormesh(x_mesh, y_mesh, intensity)
    plt.plot(x, y, 'ro')
    plt.colorbar()
    plt.title('Airline Load Factor', font='Viner Hand ITC', fontsize=15)
    plt.xlabel('Year')
    plt.ylabel('Load Factor')
    plt.show()


if __name__ == "__main__":
    read_file()
    read_file2()
    read_file3()
    read_file4()
    read_file5()