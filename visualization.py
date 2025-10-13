import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

excel_file = 'M3C.xls'
sheet_name = "M3Month"
category = "FINANCE"

# Loads the sheet we want to work with
data = pd.read_excel(excel_file, sheet_name=sheet_name)
print("Data loaded successfully!")
print("Shape:", data.shape)
print(data.head())

# Filters the data for the specified category
category_data = data[data['Category'].str.strip() == category]
print(f"Found {len(category_data)} {category} series")
print(category_data.head())

# Get the first series, it starts at column index 6
series = category_data.iloc[0, 6:].dropna().astype(float)
print(f"Selected series length: {len(series)} time points")


plt.figure(figsize=(12, 6))
plt.plot(series.values, marker='o', linewidth=2, markersize=4)
plt.title("Financial time series, monthly", fontsize=14, fontweight='bold')
plt.xlabel("Time step", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.grid(True, alpha=0.3)

# Using WSL so I need to save the plot to a file
plot_filename = 'financial_time_series.png'
plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
print(f"✓ Plot saved as '{plot_filename}'")

print(f"\nTime Series Statistics:")
print(f"  Length: {len(series)} time points")
print(f"  Mean: {series.mean():.2f}")
print(f"  Std Dev: {series.std():.2f}")
print(f"  Min: {series.min():.2f}")
print(f"  Max: {series.max():.2f}")

plt.close()  
