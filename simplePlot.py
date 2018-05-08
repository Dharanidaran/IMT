# simplePlot.py
import matplotlib.pyplot as plt
import numpy as np


#Create a single Dimensional array with numpy


y = np.arange(0.0, 10.0,1)
print(y)

x = np.arange(10)
print(x)



plt.plot(x,y)
plt.show()




#Scatter plot

print(np.square(y))
print(y)
x = np.arange(0.0,10.0,1)
y = np.square(y)


plt.plot(x,y,".",x,y**2,'bs',x,y,'g+')
plt.show()



