# Uni-Variate Linear Regression
{% include lib/mathjax.html %}
A fancy name for single independent variable linear regression where the main purpose is to find the equation ***(y = mx +b)*** for the best fit line in the available observations/data where aforementioned equation expands to:  

## y = mx + b
- y = Predicted Value
- m = Slope of the curve
- x = Input variable
- b = Y intercept

> **Calculating variables of the equation:**  
> Consider an example dataset
> | LotSize (x) | SalePrice (y) |
> | ------- | --------- |
> | 8450 | 208500 |
> | 9600 | 181500 |
> | 11250 | 223500 |
> | 9550  | 140000 |
> | 14260 | 250000 |
> | 14115 | 143000 |
> | 10084 | 307000 |
> | 10382 | 200000 |

> Where *LotSize* is an independent variable **(x)** and *SalePrice* is a dependent variable **(y)**  


> **Steps:**
> 1. Find the mean(*&mu;*) for x & y:
>>> **&mu;_x** = np.mean(x)  
>>> **&mu;_y** = np.mean(y)  
> 2. Find the standard deviation for x & y:  
>>> **&sigma;_x** = np.std(x)  
>>> **&sigma;_y** = np.std(y)  
> 3. Find Zscore for each observation in x & y:  
>>> ***Formula :***  
>>> Samples: z = x - &overline;{x}
>>> **&sigma;_x** = np.std(x)  
>>> **&sigma;_y** = np.std(y)  

	\frac{n!}{k!(n-k)!}

    $$
M = \left( \begin{array}{ccc}
x_{11} & x_{12} & \ldots \\
x_{21} & x_{22} & \ldots \\
\vdots & \vdots & \ldots \\
\end{array} \right)
$$

<img src="https://render.githubusercontent.com/render/math?math=e^{i \pi} = -1">

\Huge e^{i\pi} = -1