import snap
import re
from scipy import stats
x1 = [1,1,2,3,3]

x2 = [3,3,2,1,1]
tau, p_value = stats.kendalltau(x1, x2)

print tau, p_value


tau, p_value = stats.spearmanr(x1, x2)

print tau, p_value

