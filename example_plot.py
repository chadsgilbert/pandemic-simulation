#!/usr/bin/python

""" Create a sample plot for inclusion in my document. """

import sys
import matplotlib.pyplot as mpl


def make_plot(filename):
    """ Create the example plot. """
    plot_x = [1, 2, 3, 4, 5]
    plot_y = [6, 7, -2, 3, 5]

    mpl.plot(plot_x, plot_y)
    mpl.title("example plot")
    mpl.xlabel("x")
    mpl.ylabel("y")
    mpl.savefig(filename)


if __name__ == "__main__":
    make_plot(sys.argv[1])