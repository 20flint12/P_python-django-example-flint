"""
Reference for colormaps included with Matplotlib.

This reference example shows all colormaps included with Matplotlib. Note that
any colormap listed here can be reversed by appending "_r" (e.g., "pink_r").
These colormaps are divided into the following categories:

Sequential:
    These colormaps are approximately monochromatic colormaps varying smoothly
    between two color tones---usually from low saturation (e.g. white) to high
    saturation (e.g. a bright blue). Sequential colormaps are ideal for
    representing most scientific data since they show a clear progression from
    low-to-high values.

Diverging:
    These colormaps have a median value (usually light in color) and vary
    smoothly to two different color tones at high and low values. Diverging
    colormaps are ideal when your data has a median value that is significant
    (e.g.  0, such that positive and negative values are represented by
    different colors of the colormap).

Qualitative:
    These colormaps vary rapidly in color. Qualitative colormaps are useful for
    choosing a set of discrete colors. For example::

        color_list = plt.cm.Set3(np.linspace(0, 1, 12))

    gives a list of RGB colors that are good for plotting a series of lines on
    a dark background.

Miscellaneous:
    Colormaps that don't fit into the categories above.

"""
import numpy as np
import matplotlib.pyplot as plt


cmaps = [('Sequential',     ['Blues', 'BuGn', 'BuPu',
                             'GnBu', 'Greens', 'Greys', 'PuBu',
                             'My_graph'])]

max_point = 256

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)
gradient = np.linspace(0, 1, max_point)
gradient = np.vstack((gradient, gradient))
# print  gradient


def plot_color_gradients(cmap_category, cmap_list):
    fig, axes = plt.subplots(nrows=nrows, sharex=True, sharey=True)

    # print "axes", axes[-1:]
    # print plt.gca()

    fig.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)


    # # Three subplots sharing both x/y axes
    # f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
    # ax1.plot(x, y)
    # ax1.set_title('Sharing both axes')
    # ax2.scatter(x, y)
    # ax3.scatter(x, 2 * y ** 2 - 1, color='r')
    # # Fine-tune figure; make subplots close to each other and hide x ticks for
    # # all but bottom plot.
    # f.subplots_adjust(hspace=0)
    # plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)



    fig.subplots_adjust(top=0.98, bottom=0.05, left=0.1, right=1)
    # axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_list):

        # print "ax", ax


        if name == "My_graph":
            x = np.arange(0, max_point/10., max_point/10./256.)
            y = np.arange(0, 1, 1)
            X, Y = np.meshgrid(x,y)
            Z = np.cos(X) * 10
            ax.imshow(Z, aspect='auto', interpolation='nearest', cmap="Greys")

        else:
            ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))



        # pos = list(ax.get_position().bounds)
        # print pos
        # x_text = pos[0] - 0.01
        # y_text = pos[1] + pos[3]/2.
        # fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # axes.imshow(gradient, aspect='auto', cmap="Greys")
    # plt.gca().imshow(gradient, aspect='auto', cmap="Greys")

    #
    # x = np.arange(0, np.pi, 0.1)
    # y = np.arange(0, 2*np.pi, 0.1)
    # X, Y = np.meshgrid(x,y)
    # Z = np.cos(X) * 10
    # plt.gca().imshow(Z, interpolation='nearest', cmap="Greys")




    # Turn off *all* ticks & spines, not just the ones with colormaps.
    # for ax in axes:
    #     ax.set_axis_off()



def plot_graph():

    x = np.arange(0, np.pi, 0.1)
    y = np.arange(0, 2*np.pi, 0.1)
    X, Y = np.meshgrid(x,y)
    # print X, Y

    # Z = np.cos(X) * np.sin(Y) * 10
    Z = np.cos(X) * 10
    # print Z


    plt.subplot(2,2,1)
    plt.imshow(X, interpolation='nearest', cmap="Greys")
    # plt.colorbar()




if __name__ == '__main__':

    for cmap_category, cmap_list in cmaps:
        plot_color_gradients(cmap_category, cmap_list)

    # plot_graph()

    plt.show()
















