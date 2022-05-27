import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

y1 = float(input(Unesite visinu prvog brda ))
v1 = float(input(Unesite brzinu prvog projektila ))

v2 = float(input(Unesite brzinu drugog projektila ))
y2 = float(input(Unesite visinu drugog brda ))

d = float(input(Unesite razdaljinu izmedju dva topa ))

x1 = 1.0
x2 = x1 + d
g = 9.81

r = sqrt((d  d) + (y1 - y2)  (y1 - y2))

if y1 != y2
    if y1  y2
        ts = r  (v1 + v2)
        #s_no_gravity = (x1 + v1  ts, y1)
        #s_with_gravity = (x1 + v1  ts, y1 - ((g  ts  ts)  2))

        time = np.linspace(0, ts, 1000)

        x_l_n_g = []
        y_l_n_g = []
        x_r_n_g = []
        y_r_n_g = []

        x_l_g = []
        y_l_g = []
        x_r_g = []
        y_r_g = []

        for t in time
            x_l_n_g.append(x1 + v1  (d  r)  t)
            y_l_n_g.append(y1 - v1  ((y1 - y2)  r)  t)
            x_r_n_g.append(x2 - v2  (d  r)  t)
            y_r_n_g.append(y2 - v2  ((y1 - y2)  r)  t)

            x_l_g.append(x1 + v1  (d  r)  t)
            y_l_g.append(y1 - v1  ((y1 - y2)  r)  t - (g  t  t)  2)
            x_r_g.append(x2 - v2  (d  r)  t)
            y_r_g.append(y2 - v2  ((y1 - y2)  r)  t - (g  t  t)  2)

        plt.figure(1)
        plt.plot(x_l_n_g, y_l_n_g)
        plt.plot(x_r_n_g, y_r_n_g)
        plt.show()

        plt.figure(2)
        plt.plot(x_l_g, y_l_g)
        plt.plot(x_r_g, y_r_g)
        plt.show()
    else
        pass
else
    ts = d  (v1 + v2)
    s_no_gravity = (x1 + v1  ts, y1)
    s_with_gravity = (x1 + v1  ts, y1 - ((g  ts  ts)  2))

    time = np.linspace(0, ts, 1000)

    x_l_n_g = []
    y_l_n_g = []
    x_r_n_g = []
    y_r_n_g = []

    x_l_g = []
    y_l_g = []
    x_r_g = []
    y_r_g = []

    for t in time
        x_l_n_g.append(x1 + v1  t)
        y_l_n_g.append(y1)
        x_r_n_g.append(x2 - v2  t)
        y_r_n_g.append(y2)

        x_l_g.append(x1 + v1  t)
        y_l_g.append(y1 - (g  (t  t))  2)
        x_r_g.append(x2 - v2  t)
        y_r_g.append(y2 - (g  (t  t))  2)

    plt.figure(1)
    plt.plot(x_l_n_g, y_l_n_g)
    plt.plot(x_r_n_g, y_r_n_g)
    plt.show()

    plt.figure(2)
    plt.plot(x_l_g, y_l_g)
    plt.plot(x_r_g, y_r_g)
    plt.show()