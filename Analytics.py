# Pandas :
Pandas is a Python library used for data manipulation and analysis. 
It provides easy-to-use data structures like Series (1D) and DataFrame (2D) to handle and analyze structured data efficiently.

Pandas helps you clean, filter, analyze, and visualize data easily — just like working with an Excel sheet but using Python code.

import pandas as pd

data = {'Name': ['A', 'B', 'C'], 'Age': [20, 25, 30]}
df = pd.DataFrame(data)
print(df)

# NumPy:
NumPy (Numerical Python) is a Python library used for numerical and scientific computing. 
It provides powerful n-dimensional arrays (ndarray) and supports fast mathematical operations like mean, median, matrix multiplication, etc.
                                                                                                                                      
NumPy helps you perform fast mathematical calculations on large amounts of numerical data.

import numpy as np

arr = np.array([1, 2, 3, 4])
print(np.mean(arr))   # Output: 2.5

🧩 Difference in one line
Library	Purpose
NumPy	Works with numerical data (arrays & matrices)
Pandas	Works with structured data (tables/dataframes)

