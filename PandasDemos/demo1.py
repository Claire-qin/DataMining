import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull


points = np.random.rand(30, 2)
hull = ConvexHull(points)
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.show()

plt.scatter()

data = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
data.reset_index()
data.sort_values()

a1 = [1,2,3]
a2 = [4,5,6]
np.r_(a1,a2)
np.concatenate()
np.append()
np.stack()
np.hstack()
pd.cut()


