import pandas as pd
import numpy as np
import scipy.stats as sps


chat_id = 1260358058 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    pvalue = sps.ttest_ind(x, y).pvalue
    return pvalue < alpha
