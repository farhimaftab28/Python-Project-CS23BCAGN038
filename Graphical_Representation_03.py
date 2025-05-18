import matplotlib.pyplot as plt    # type: ignore
import numpy as np                # type: ignore

x = np.linspace(-10, 10, 100)
y = x**2 - 4*x + 3
plt.plot(x, y, color='blue')  

plt.title("Graph of y = x² - 4x + 3")
plt.xlabel("X value")         
plt.ylabel("Y value")         

plt.grid(True)
plt.show()
