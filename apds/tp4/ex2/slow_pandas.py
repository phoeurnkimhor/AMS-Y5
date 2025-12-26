import pandas as pd
import numpy as np
import time

# Start total timer
total_start = time.perf_counter()

# 1. CSV loading
start = time.perf_counter()
df = pd.read_csv("diabetes_dataset.csv")
end = time.perf_counter()
print(f"CSV loading time: {end - start:.6f} seconds")

# 2. Age grouping
start = time.perf_counter()
df['AgeGroup'] = pd.cut(df['age'], bins=[0,30,60,np.inf], labels=['Young','Middle','Old'])
end = time.perf_counter()
print(f"Age grouping time: {end - start:.6f} seconds")

# 3. Column math operations
start = time.perf_counter()
df['BMI_Squared'] = df['bmi']**2
df['Glucose_Adjusted'] = df['blood_glucose_level']/18.0
df['RiskScore'] = (df['bmi'] + df['blood_glucose_level'] + df['hbA1c_level'])/3
end = time.perf_counter()
print(f"Column math operations time: {end - start:.6f} seconds")

# 4. RiskFlag calculation
start = time.perf_counter()
conditions = [
    (df['blood_glucose_level']>140) & (df['bmi']>30),
    (df['blood_glucose_level']>120)
]
choices = ['High','Medium']
df['RiskFlag'] = np.select(conditions, choices, default='Low')
end = time.perf_counter()
print(f"RiskFlag calculation time: {end - start:.6f} seconds")

# 5. Merge operation
start = time.perf_counter()
temp = df[['year','RiskFlag']].drop_duplicates()
df = df.merge(temp, on='year', how='left')
end = time.perf_counter()
print(f"Merge operation time: {end - start:.6f} seconds")

# Total runtime
total_end = time.perf_counter()
print(f"Total runtime: {total_end - total_start:.8f} seconds")
