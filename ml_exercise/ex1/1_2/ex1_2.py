import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

# ランダムに観測点を用意
np.random.seed(0)
x_obs = np.random.uniform(-1, 1, size=20)
# 真値を計算
y_true = true_function(x_obs)
# DataFrameを作成
df = pd.DataFrame({'観測点': x_obs, '真値': y_true})
print(df)

x = np.linspace(-1, 1, num=100)
y = true_function(x)
plt.plot(x, y, label='true value')
plt.scatter(x_obs, y_true, label='Observation point', color = 'red')
plt.legend()
plt.savefig('ex1.2.png')
plt.show()


