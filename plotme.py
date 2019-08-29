import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
matplotlib.rc('font',**{'family':'serif','serif':['Palatino']})
matplotlib.rc('text', usetex=True)


fig = plt.figure()
ax = plt.axes()
ax.axis('equal')
ax.spines['top'].set_position(('data', 1.1))
ax.xaxis.set_ticks_position('top')
ax.spines['left'].set_position(('data', -1.0))
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)

dx = 0.15
offset = matplotlib.transforms.ScaledTranslation(
    dx, 0.0, fig.dpi_scale_trans)
for label in ax.xaxis.get_majorticklabels():
    label.set_transform(label.get_transform() + offset)

x = np.linspace(-1.0, 1.0, 300)
xp = np.linspace(-0.1, 0.1, 100)
y1 = np.vectorize(lambda q: math.sqrt(1.0 - q * q))
y2 = np.vectorize(lambda q: -math.sqrt(1.0 - q * q))
y3 = np.vectorize(lambda q: 200.0 * q * q - 1.0) 
ax.plot(x, y1(x), color='blue', linewidth=3)
line1, = ax.plot(x, y2(x), color='blue', linewidth=3)
line2, = ax.plot(xp, y3(xp), color='red', linewidth=3)
ax.legend((line1, line2), ('$x^{2}+y^{2}=1$', '$y=cx^2-1$'),
          loc='upper center', bbox_to_anchor=(0.5, 0.2),
          fancybox=True, framealpha=0.0)
fig = plt.gcf()
fig.subplots_adjust(top=1.1)
fig.set_size_inches(2.2, 2.8)
plt.savefig('circ-parab.png', transparent=True)
