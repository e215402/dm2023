import numpy as np
import matplotlib.pyplot as plt

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

# グラフの描画
x = np.linspace(-1, 1, num=100)
y = true_function(x)
plt.plot(x, y, label="True function")
plt.legend()
plt.savefig("ex1.1.png")
plt.show()
