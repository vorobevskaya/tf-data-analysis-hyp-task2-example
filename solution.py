import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 689606612 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    p = ks_2samp(x, y, alternative="two-sided").pvalue
    if p >= 0.06:
      result = bool(0)
    else:
      result = bool(1)
    return result # Ваш ответ, True или False
