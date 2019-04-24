import numpy as np

import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

line1, line2 = plt.plot(t, t, t, t**2)

print(plt.setp(line1))
# plt.setp(line1, color='r', linewidth=2.0)
# plt.setp(line2, color='g', linewidth=1.5)

plt.show()