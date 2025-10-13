import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

excel_file = 'M3C.xls'
sheet_name = "M3Month"
category = "FINANCE"

# Loads the sheet we want to work with
data = pd.read_excel(excel_file, sheet_name=sheet_name)
print(data.head())

# Filters the data for the specified category
category_data = data[data['Category'] == category]
print(category_data.head())

