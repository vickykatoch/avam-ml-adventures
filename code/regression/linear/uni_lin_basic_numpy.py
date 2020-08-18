import numpy as np
from os import path
import matplotlib.pyplot as plt
import code.common.linreg as linear_reg

# LOAD THE DATA
filepath = path.join(path.dirname(__file__),'../../../data/basic/housing-data.csv')
data = np.genfromtxt(filepath, delimiter = ',', skip_header=1)

# GET X & Y
x = data[:,0]
y = data[:,1]

result = linear_reg.fit_uni_variate(x,y)
slope = result['slope']
icept = result['intercept']

# CALC PREDICTIONS ON THE BASIS OF EQUATION 
# y = mx + b
predictions = slope* x + icept

# PLOT THE X,Y VALUES AND FITTED LINE
plt.scatter(x, y)
plt.xlabel('Area')
plt.ylabel('Cost')
plt.title(f'Slope : {slope}.x +  Intercept : {icept}')
plt.plot(x, predictions, color='g')
plt.show()