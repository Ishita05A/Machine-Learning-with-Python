import numpy as np
import matplotlib.pyplot as plt
dataset = [11, 10, 12, 14, 12, 15, 14, 13, 15, 102, 12, 14, 17, 19, 107, 10,
           13, 12, 14, 12, 108, 12, 11, 14, 13, 15, 10, 15, 12, 10, 14, 13, 15, 10]
sorted(dataset)
quantile1, quantile3 = np.percentile(dataset, [25, 75])
print(quantile1, quantile3)
iqr_value = quantile3-quantile1
print(iqr_value)
lower_bound_val = quantile1 - (1.5 * iqr_value)
upper_bound_val = quantile3 + (1.5 * iqr_value)
print(lower_bound_val, upper_bound_val)
