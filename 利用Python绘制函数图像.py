import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,2*np.pi,0.01)
y1=np.six(x)
y2=np.six(-x)
y3=np.six(2*x)/2
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.title('sinx(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
