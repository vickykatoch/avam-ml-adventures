import numpy as np

data = np.array([ [ 8450 	,208500],
[9600 	,181500],
[11250 	,223500],
[9550 	,140000],
[14260 	,250000],
[14115 	,143000],
[10084 	,307000],
[10382, 	200000]])

# Get X & Y

x = data[:,0]
y = data[:,1]

x_mean = x.mean()
y_mean = y.mean()

x_sd = x.std()
y_sd = y.std()

x_zscore = (x_mean - x).sum()/x_sd
y_zscore = (y_mean - y).sum()/y_sd



print(x_zscore)
