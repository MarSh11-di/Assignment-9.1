import numpy as np
import pandas as pd

arr_1_d = np.array([1,2,3,4,5])
arr_1_d_2 = np.arange(1,6)
print(type(arr_1_d), arr_1_d )
print(type(arr_1_d_2), arr_1_d_2)

# Create a 2D numpy array with shape (3, 5) filled with random integers between 1 and 100.
res3 = np.random.randint(1,100,(3,5))
print(res3)
# Print the first row of array res3.
print(res3[0])
# Access the last column of array res3. Assume that the array may be of any 2D shape.
print(res3[:,-1])
# Find the min, max, and sum of elements of the second column of array res3.
sum_el = np.sum(res3[:,1:2])
min_el = np.min(res3[:,1:2])
max_el = np.max(res3[:,1:2])
print(sum_el)
print(min_el)
print(max_el)
# To tabulate the function f(x)=e2x on the interval[0,1]with a step of 0.1
x = np.arange(0,1.1,0.1)
x_f = np.exp(2*x)
print(x_f)

# PANDAS
df = pd.read_csv("https://web.stanford.edu/class/cs102/datasets/Titanic.csv")

# Let's see the series/columns present in the data frame.Also, let's inspect the first ten rows of data.
print(df.columns)
print(df.head(10))

# Add a new column - full name - it should be a concat of the first and last name.
df["full_name"] = df["first"] +" " + df["last"]
print(df.columns)

# Remove the two original columns - last, first.
df.drop(["last","first"], axis=1, inplace= True )
print(df.columns)

# Calculate the total number of survivors in the dataset.
total_life = df["survived"].value_counts().get("yes",0)
print(f"Total number of survivors on the Titanic: {total_life}")