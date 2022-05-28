import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

def show_plots(x_l_n_g, y_l_n_g, x_r_n_g, y_r_n_g, x_l_g, y_l_g, x_r_g, y_r_g, s_no_gravity, s_with_gravity, left_cannon_pos, right_cannon_pos):
    plt.figure("Bez gravitacije")
    plt.title('Kretanje projektila bez uticaja gravitacije')
    plt.xlabel('Horizontalna pozicija projektila izražena u metrima')
    plt.ylabel('Vertikalna pozicija projektila izražena u metrima')

    plt.plot(x_l_n_g, y_l_n_g, color="blue")
    plt.plot(x_r_n_g, y_r_n_g, color="red")
    plt.hlines(y=0, xmin=left_cannon_pos[0], xmax=right_cannon_pos[0], color='k', linestyle='--')

    plt.scatter(left_cannon_pos[0], left_cannon_pos[1]);
    plt.scatter(right_cannon_pos[0], right_cannon_pos[1]);
    plt.scatter(s_no_gravity[0], s_no_gravity[1], color="m");
    plt.annotate("A", left_cannon_pos, color='blue');
    plt.annotate("B", right_cannon_pos, color='red');
    plt.annotate("S", s_no_gravity, color='m');
    plt.annotate("Ground", ((right_cannon_pos[0] - left_cannon_pos[0]) / 2, 0), ha='center');

    plt.figure("Sa gravitacijom")
    plt.title('Kretanje projektila pod uticajem gravitacije')
    plt.xlabel('Horizontalna pozicija projektila izražena u metrima')
    plt.ylabel('Vertikalna pozicija projektila izražena u metrima')

    plt.plot(x_l_g, y_l_g, color="blue")
    plt.plot(x_r_g, y_r_g, color="red")
    plt.hlines(y=0, xmin=left_cannon_pos[0], xmax=right_cannon_pos[0], color='k', linestyle='--')

    plt.scatter(left_cannon_pos[0], left_cannon_pos[1]);
    plt.scatter(right_cannon_pos[0], right_cannon_pos[1]);
    plt.scatter(s_with_gravity[0], s_with_gravity[1], color="m");
    plt.annotate("A", left_cannon_pos, color='blue');
    plt.annotate("B", right_cannon_pos, color='red');
    plt.annotate("S", s_with_gravity, color='m');
    plt.annotate("Ground", ((right_cannon_pos[0] - left_cannon_pos[0]) / 2, 0), ha='center');
    plt.show()

y1 = float(input("Unesite visinu prvog brda izrazenu u metrima: "))
v1 = float(input("Unesite brzinu prvog projektila izrazenu u m/s: "))

y2 = float(input("Unesite visinu drugog brda izrazenu u metrima: "))
v2 = float(input("Unesite brzinu drugog projektila izrazenu u m/s: "))

d = float(input("Unesite razdaljinu izmedju dva topa izrazenu u metrima: "))

x1 = 0.0
x2 = x1 + d
g = 9.81

r = sqrt((d ** 2) + (y1 - y2) ** 2)

x_l_n_g = []
y_l_n_g = []
x_r_n_g = []
y_r_n_g = []

x_l_g = []
y_l_g = []
x_r_g = []
y_r_g = []

if y1 != y2:
    if y1 > y2:
        ts = r / (v1 + v2)
        s_no_gravity = (x1 + v1 * (d / (v1 + v2)), y1 - v1 * ((y1 - y2) / (v1 + v2)))
        s_with_gravity = (x1 + v1 * (d / (v1 + v2)), y1 - v1 * ((y1 - y2) / (v1 + v2)) - (g * (ts ** 2)) / 2)

        time = np.linspace(0, ts, 1000)

        for t in time:
            x_l_n_g.append(x1 + v1 * (d / r) * t)
            y_l_n_g.append(y1 - v1 * ((y1 - y2) / r) * t)
            x_r_n_g.append(x2 - v2 * (d / r) * t)
            y_r_n_g.append(y2 + v2 * ((y1 - y2) / r) * t)

            x_l_g.append(x1 + v1 * (d / r) * t)
            y_l_g.append(y1 - v1 * ((y1 - y2) / r) * t - (g * (t ** 2) / 2))
            x_r_g.append(x2 - v2 * (d / r) * t)
            y_r_g.append(y2 + v2 * ((y1 - y2) / r) * t - (g * (t ** 2) / 2))

        show_plots(x_l_n_g, y_l_n_g, x_r_n_g, y_r_n_g, x_l_g, y_l_g, x_r_g, y_r_g, s_no_gravity, s_with_gravity, (x1, y1), (x2, y2))
    else:
        ts = r / (v1 + v2)
        s_no_gravity = (x1 + v1 * (d / (v1 + v2)), y1 + v1 * ((y2 - y1) / (v1 + v2)))
        s_with_gravity = (x1 + v1 * (d / (v1 + v2)), y1 + v1 * ((y2 - y1) / (v1 + v2)) - (g * (ts ** 2)) / 2)
        time = np.linspace(0, ts, 1000)

        for t in time:
            x_l_n_g.append(x1 + v1 * (d / r) * t)
            y_l_n_g.append(y1 + v1 * ((y2 - y1) / r) * t)
            x_r_n_g.append(x2 - v2 * (d / r) * t)
            y_r_n_g.append(y2 - v2 * ((y2 - y1) / r) * t)

            x_l_g.append(x1 + v1 * (d / r) * t)
            y_l_g.append(y1 + v1 * ((y2 - y1) / r) * t - (g * (t ** 2) / 2))
            x_r_g.append(x2 - v2 * (d / r) * t)
            y_r_g.append(y2 - v2 * ((y2 - y1) / r) * t - (g * (t ** 2) / 2))

        show_plots(x_l_n_g, y_l_n_g, x_r_n_g, y_r_n_g, x_l_g, y_l_g, x_r_g, y_r_g, s_no_gravity, s_with_gravity, (x1, y1), (x2, y2))
else:
    ts = d / (v1 + v2)
    s_no_gravity = (x1 + v1 * ts, y1)
    s_with_gravity = (x1 + v1 * ts, y1 - (g * (ts ** 2) / 2))

    time = np.linspace(0, ts, 1000)

    for t in time:
        x_l_n_g.append(x1 + v1 * t)
        y_l_n_g.append(y1)
        x_r_n_g.append(x2 - v2 * t)
        y_r_n_g.append(y2)

        x_l_g.append(x1 + v1 * t)
        y_l_g.append(y1 - (g * (t ** 2)) / 2)
        x_r_g.append(x2 - v2 * t)
        y_r_g.append(y2 - (g * (t ** 2)) / 2)

    show_plots(x_l_n_g, y_l_n_g, x_r_n_g, y_r_n_g, x_l_g, y_l_g, x_r_g, y_r_g, s_no_gravity, s_with_gravity, (x1, y1), (x2, y2))
    
