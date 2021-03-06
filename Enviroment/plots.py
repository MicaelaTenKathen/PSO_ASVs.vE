import matplotlib.pyplot as plt
from Data_scripts.data_bound import Z_var_mean
import numpy as np
import matplotlib.ticker as ticker


def plot_evolucion(log):
    gen = log.select("gen")
    fit_mins = log.select("min")
    fit_maxs = log.select("max")
    fit_ave = log.select("avg")

    fig, ax1 = plt.subplots()
    ax1.plot(gen, fit_mins, "b")
    ax1.plot(gen, fit_maxs, "r")
    ax1.plot(gen, fit_ave, "--k")
    ax1.fill_between(gen, fit_mins, fit_maxs,
                     where=fit_maxs >= fit_mins,
                     facecolor="g", alpha=0.2)
    ax1.set_xlabel("Generación")
    ax1.set_ylabel("Fitness")
    ax1.legend(["Min", "Max", "Avg"])
    plt.grid(True)


def plot_movimiento(x_a, y_a):
    plt.figure(2)
    plt.scatter(x_a, y_a)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.title("Movimiento de las partículas")
    plt.show()
    plt.close()


def bench_plot(xs, ys, bench_function, X_test, grid):
    plot = np.zeros([xs, ys])
    for i in range(len(X_test)):
        plot[X_test[i][0], X_test[i][1]] = bench_function[i]
    plot[grid == 0] = np.nan
    benchma_plot = plot.T
    return plot, benchma_plot


def plot_gaussian(ys, x_ga, y_ga, n, mu, sigma, X_test, grid, grid_min, part_ant):
    Z_var, Z_mean = Z_var_mean(mu, sigma, X_test, grid)

    fig, axs = plt.subplots(2, 1, figsize=(5, 10))

    im1 = axs[0].scatter(x_ga, y_ga, c=n, cmap="gist_rainbow", marker='.')
    p1x = list(map(lambda x: x + abs(grid_min), part_ant[:, 0]))
    p1y = list(map(lambda x: x + abs(grid_min), part_ant[:, 1]))
    axs[0].plot(p1x, p1y, 'r')
    p2x = list(map(lambda x: x + abs(grid_min), part_ant[:, 2]))
    p2y = list(map(lambda x: x + abs(grid_min), part_ant[:, 3]))
    axs[0].plot(p2x, p2y, 'w')
    p3x = list(map(lambda x: x + abs(grid_min), part_ant[:, 4]))
    p3y = list(map(lambda x: x + abs(grid_min), part_ant[:, 5]))
    axs[0].plot(p3x, p3y, 'c')
    p4x = list(map(lambda x: x + abs(grid_min), part_ant[:, 6]))
    p4y = list(map(lambda x: x + abs(grid_min), part_ant[:, 7]))
    axs[0].plot(p4x, p4y, 'k')

    im2 = axs[0].imshow(Z_var.T, interpolation='bilinear', origin='lower', cmap="viridis")
    # plt.colorbar(im2, ax=axs[0], format='%.2f', label='σ', shrink=1.0)
    # axs[0].set_xlabel("x [m]")
    axs[0].set_ylabel("y [m]")
    axs[0].set_yticks([0, 20, 40, 60, 80, 100, 120, 140])
    axs[0].set_xticks([0, 50, 100])
    axs[0].set_aspect('equal')
    axs[0].set_ylim([ys, 0])
    axs[0].grid(True)
    ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x * 100))
    axs[0].xaxis.set_major_formatter(ticks_x)

    ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x * 100))
    axs[0].yaxis.set_major_formatter(ticks_y)

    im3 = axs[1].imshow(Z_mean.T, interpolation='bilinear', origin='lower', cmap="jet")
    # plt.colorbar(im3, ax=axs[1], format='%.2f', label='µ', shrink=1.0)
    axs[1].set_xlabel("x [m]")
    axs[1].set_ylabel("y [m]")
    axs[1].set_ylim([ys, 0])
    axs[1].set_aspect('equal')
    axs[1].grid(True)
    ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x * 100))
    axs[1].xaxis.set_major_formatter(ticks_x)

    ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x * 100))
    axs[1].yaxis.set_major_formatter(ticks_y)

    # fig.savefig("STD, MEAN", dpi=200)
    plt.show()


def plot_benchmark(xs, ys, grid, bench_function, X_test):
    plot, benchmark_plot = bench_plot(xs, ys, bench_function, X_test, grid)

    fig = plt.figure(2)
    ax1 = fig.add_subplot(121)
    im4 = ax1.imshow(benchmark_plot, interpolation='bilinear', origin='lower', cmap="jet")
    plt.colorbar(im4, format='%.2f', label='µ', shrink=1)
    ax1.set_xlabel("x [m]")
    ax1.set_ylabel("y [m]")
    ax1.set_ylim([ys, 0])
    ax1.set_aspect('equal')
    ax1.grid(True)
    ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x * 100))
    ax1.xaxis.set_major_formatter(ticks_x)

    ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x * 100))
    ax1.yaxis.set_major_formatter(ticks_y)
    return plot


def plot_error(MSE_data, it, GEN):
    plt.figure(3)
    plt.plot(it, MSE_data, '-')
    plt.xlabel("Iterations")
    plt.ylabel("MSE")
    plt.xlim([0, GEN])
    plt.grid(True)
    plt.title("Mean Square Error")
    # plt.savefig("MSE", dpi=200)
    plt.show()
