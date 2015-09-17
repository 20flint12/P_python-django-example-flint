# """
# Reference for colormaps included with Matplotlib.
#
# This reference example shows all colormaps included with Matplotlib. Note that
# any colormap listed here can be reversed by appending "_r" (e.g., "pink_r").
# These colormaps are divided into the following categories:
#
# Sequential:
#     These colormaps are approximately monochromatic colormaps varying smoothly
#     between two color tones---usually from low saturation (e.g. white) to high
#     saturation (e.g. a bright blue). Sequential colormaps are ideal for
#     representing most scientific data since they show a clear progression from
#     low-to-high values.
#
# Diverging:
#     These colormaps have a median value (usually light in color) and vary
#     smoothly to two different color tones at high and low values. Diverging
#     colormaps are ideal when your data has a median value that is significant
#     (e.g.  0, such that positive and negative values are represented by
#     different colors of the colormap).
#
# Qualitative:
#     These colormaps vary rapidly in color. Qualitative colormaps are useful for
#     choosing a set of discrete colors. For example::
#
#         color_list = plt.cm.Set3(np.linspace(0, 1, 12))
#
#     gives a list of RGB colors that are good for plotting a series of lines on
#     a dark background.
#
# Miscellaneous:
#     Colormaps that don't fit into the categories above.
#
# """
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# cmaps = [('Sequential',     ['Blues', 'BuGn', 'BuPu',
#                              'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
#                              'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
#                              'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
#          ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool', 'copper',
#                              'gist_heat', 'gray', 'hot', 'pink',
#                              'spring', 'summer', 'winter']),
#          ('Diverging',      ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
#                              'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
#                              'seismic']),
#          ('Qualitative',    ['Accent', 'Dark2', 'Paired', 'Pastel1',
#                              'Pastel2', 'Set1', 'Set2', 'Set3']),
#          ('Miscellaneous',  ['gist_earth', 'terrain', 'ocean', 'gist_stern',
#                              'brg', 'CMRmap', 'cubehelix',
#                              'gnuplot', 'gnuplot2', 'gist_ncar',
#                              'nipy_spectral', 'jet', 'rainbow',
#                              'gist_rainbow', 'hsv', 'flag', 'prism'])]
#
#
# nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)
# gradient = np.linspace(0, 1, 256)
# gradient = np.vstack((gradient, gradient))
#
# def plot_color_gradients(cmap_category, cmap_list):
#     fig, axes = plt.subplots(nrows=nrows)
#     fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
#     axes[0].set_title(cmap_category + ' colormaps', fontsize=14)
#
#     for ax, name in zip(axes, cmap_list):
#         ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
#         pos = list(ax.get_position().bounds)
#         print pos
#         x_text = pos[0] - 0.01
#         y_text = pos[1] + pos[3]/2.
#         fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)
#
#     # Turn off *all* ticks & spines, not just the ones with colormaps.
#     for ax in axes:
#         ax.set_axis_off()
#
# for cmap_category, cmap_list in cmaps:
#     plot_color_gradients(cmap_category, cmap_list)
#
# plt.show()


#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

"""

Example: suppose you want red to increase from 0 to 1 over the bottom
half, green to do the same over the middle half, and blue over the top
half.  Then you would use:

cdict = {'red':   ((0.0,  0.0, 0.0),
                   (0.5,  1.0, 1.0),
                   (1.0,  1.0, 1.0)),

         'green': ((0.0,  0.0, 0.0),
                   (0.25, 0.0, 0.0),
                   (0.75, 1.0, 1.0),
                   (1.0,  1.0, 1.0)),

         'blue':  ((0.0,  0.0, 0.0),
                   (0.5,  0.0, 0.0),
                   (1.0,  1.0, 1.0))}

If, as in this example, there are no discontinuities in the r, g, and b
components, then it is quite simple: the second and third element of
each tuple, above, is the same--call it "y".  The first element ("x")
defines interpolation intervals over the full range of 0 to 1, and it
must span that whole range.  In other words, the values of x divide the
0-to-1 range into a set of segments, and y gives the end-point color
values for each segment.

Now consider the green. cdict['green'] is saying that for
0 <= x <= 0.25, y is zero; no green.
0.25 < x <= 0.75, y varies linearly from 0 to 1.
x > 0.75, y remains at 1, full green.

If there are discontinuities, then it is a little more complicated.
Label the 3 elements in each row in the cdict entry for a given color as
(x, y0, y1).  Then for values of x between x[i] and x[i+1] the color
value is interpolated between y1[i] and y0[i+1].

Going back to the cookbook example, look at cdict['red']; because y0 !=
y1, it is saying that for x from 0 to 0.5, red increases from 0 to 1,
but then it jumps down, so that for x from 0.5 to 1, red increases from
0.7 to 1.  Green ramps from 0 to 1 as x goes from 0 to 0.5, then jumps
back to 0, and ramps back to 1 as x goes from 0.5 to 1.

row i:   x  y0  y1
                /
               /
row i+1: x  y0  y1

Above is an attempt to show that for x in the range x[i] to x[i+1], the
interpolation is between y1[i] and y0[i+1].  So, y0[0] and y1[-1] are
never used.

"""



cdict1 = {'red':   ((0.0, 0.0, 0.0),
                   (0.5, 0.0, 0.1),
                   (1.0, 1.0, 1.0)),

         'green': ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0)),

         'blue':  ((0.0, 0.0, 1.0),
                   (0.5, 0.1, 0.0),
                   (1.0, 0.0, 0.0))
        }

cdict2 = {'red':   ((0.0, 0.0, 0.0),
                   (0.5, 0.0, 1.0),
                   (1.0, 0.1, 1.0)),

         'green': ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0)),

         'blue':  ((0.0, 0.0, 0.1),
                   (0.5, 1.0, 0.0),
                   (1.0, 0.0, 0.0))
        }

cdict3 = {'red':  ((0.0, 0.0, 0.0),
                   (0.25,0.0, 0.0),
                   (0.5, 0.8, 1.0),
                   (0.75,1.0, 1.0),
                   (1.0, 0.4, 1.0)),

         'green': ((0.0, 0.0, 0.0),
                   (0.25,0.0, 0.0),
                   (0.5, 0.9, 0.9),
                   (0.75,0.0, 0.0),
                   (1.0, 0.0, 0.0)),

         'blue':  ((0.0, 0.0, 0.4),
                   (0.25,1.0, 1.0),
                   (0.5, 1.0, 0.8),
                   (0.75,0.0, 0.0),
                   (1.0, 0.0, 0.0))
        }

# Make a modified version of cdict3 with some transparency
# in the middle of the range.
cdict4 = cdict3.copy()
cdict4['alpha'] = ((0.0, 1.0, 1.0),
                #   (0.25,1.0, 1.0),
                   (0.5, 0.3, 0.3),
                #   (0.75,1.0, 1.0),
                   (1.0, 1.0, 1.0))


# Now we will use this example to illustrate 3 ways of
# handling custom colormaps.
# First, the most direct and explicit:

blue_red1 = LinearSegmentedColormap('BlueRed1', cdict1)

# Second, create the map explicitly and register it.
# Like the first method, this method works with any kind
# of Colormap, not just
# a LinearSegmentedColormap:

blue_red2 = LinearSegmentedColormap('BlueRed2', cdict2)
plt.register_cmap(cmap=blue_red2)

# Third, for LinearSegmentedColormap only,
# leave everything to register_cmap:

plt.register_cmap(name='BlueRed3', data=cdict3) # optional lut kwarg
plt.register_cmap(name='BlueRedAlpha', data=cdict4)

# Make some illustrative fake data:

x = np.arange(0, np.pi, 0.01)
y = np.arange(0, 2*np.pi, 0.01)
X, Y = np.meshgrid(x,y)
# Z = np.cos(X) * np.sin(Y) * 10
Z = np.cos(X) * 10

# Make the figure:

plt.figure(figsize=(6,9))
plt.subplots_adjust(left=0.02, bottom=0.06, right=0.95, top=0.94, wspace=0.05)

# Make 4 subplots:

plt.subplot(2,2,1)
plt.imshow(X, interpolation='nearest', cmap=blue_red1)
plt.colorbar()

plt.subplot(2,2,2)
cmap = plt.get_cmap('Greys')
plt.imshow(Z, interpolation='nearest', cmap=cmap)
# plt.colorbar()

# Now we will set the third cmap as the default.  One would
# not normally do this in the middle of a script like this;
# it is done here just to illustrate the method.

plt.rcParams['image.cmap'] = 'BlueRed3'

plt.subplot(2,2,3)
plt.imshow(Z, interpolation='nearest')
plt.colorbar()
plt.title("Alpha = 1")

# Or as yet another variation, we can replace the rcParams
# specification *before* the imshow with the following *after*
# imshow.
# This sets the new default *and* sets the colormap of the last
# image-like item plotted via pyplot, if any.
#

plt.subplot(2,2,4)
# Draw a line with low zorder so it will be behind the image.
plt.plot([0, 10*np.pi], [0, 20*np.pi], color='c', lw=20, zorder=-1)

plt.imshow(Z, interpolation='nearest')
plt.colorbar()

# Here it is: changing the colormap for the current image and its
# colorbar after they have been plotted.
plt.set_cmap('BlueRedAlpha')
plt.title("Varying alpha")
#

plt.suptitle('Custom Blue-Red colormaps', fontsize=16)

plt.show()
