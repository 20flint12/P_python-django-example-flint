# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# C, S = np.cos(X), np.sin(X)
#
# plt.plot(X, C)
# plt.plot(X, S)
#
# plt.show()


# Import `pyplot`
import matplotlib.pyplot as plt

# Initialize a Figure
fig = plt.figure()


# Add Axes to the Figure
fig.add_axes([0, 0, 1, 1])

plt.show()

print(fig)
