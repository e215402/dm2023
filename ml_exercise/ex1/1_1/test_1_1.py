import numpy as np
from ex1_1 import true_function

# テスト
def test_true_function():
    x = np.array([0])
    y = true_function(x)
    assert y == 0

