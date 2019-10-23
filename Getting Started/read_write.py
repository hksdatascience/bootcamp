# Import pandas library
import pandas as pd

# Read iris dataset and store as df
df = pd.read_csv('iris.csv')

# Summarize fields (numeric only)
df.describe()

# Write df object and save as iris2.csv
df.to_csv('iris2.csv', index = False)
