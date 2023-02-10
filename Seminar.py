import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100,100,0.01)

fig = plt.figure(figsize= (10,10))
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

def func(x):
    a = np.cos(x)
    y = -12*(x**4)*np.sin(a) - 18*(x**3) + 5*(x**2) + 10*x -30
    return y

plt.plot(x,func(x),'b')
plt.grid()

plt.legend()
plt.grid(True, linestyle=":")
plt.xlim([-100,100])
plt.ylim([-100,100])

plt.xlabel('X')
plt.ylabel('Y')

plt.show()

# min_y = min(y)
# print(min_y)
# min_x = 