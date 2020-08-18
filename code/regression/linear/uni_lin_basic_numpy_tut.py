import numpy as np
from os import path
import matplotlib.pyplot as plt

# LOAD THE DATA
filepath = path.join(path.dirname(__file__),'../../../data/basic/housing-data.csv')
data = np.genfromtxt(filepath, delimiter = ',', skip_header=1)

# GET X & Y
x = data[:,0]
y = data[:,1]

# CALC MEAN OF X & Y
x_mean=x.mean()
y_mean = y.mean()
print(f'Mean [X,Y] : [{x_mean}, {y_mean}]')

# CALC STANDARD DEVIATION OF X & Y
x_sd = x.std()
y_sd = y.std()

print(f'STD Dev [X,Y] : [{x_sd}, {y_sd}]')
# CALC Z-SCORE OF X & Y
x_zs = (x_mean - x)/x_sd
y_zs = (y_mean - y)/y_sd

# CALC CO-RELATION COFFICIENTS FOR X & Y
cor_coff = (x_zs * y_zs).sum() / len(x)
print(F'Corelation Coff : {cor_coff}')

# CALC SLOPE
# slope (m) = cor_coff * y_sd/x_sd
slope_m = cor_coff * y_sd/x_sd

# CALC INTERCEPT
#intercept (b) = y_mean - slope * x_mean
intercept_b = y_mean - slope_m * x_mean

print(f'Intercept : {intercept_b}, Slope : {slope_m}')

# CALC PREDICTIONS ON THE BASIS OF EQUATION 
# y = mx + b
predictions = slope_m * x + intercept_b

# PLOT THE X,Y VALUES AND FITTED LINE
plt.scatter(x, y)
plt.xlabel('Area')
plt.ylabel('Cost')
plt.title(f'Slope : {slope_m}.x +  Intercept : {intercept_b}')
plt.plot(x, predictions, color='g')
plt.show()



