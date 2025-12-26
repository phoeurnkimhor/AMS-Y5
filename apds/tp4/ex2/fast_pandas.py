import pandas as pd
import numpy as np
import time

start = time.perf_counter()

df = pd.read_csv("diabetes_dataset.csv")

df['AgeGroup'] = pd.cut(df['age'], bins=[0,30,60,np.inf], labels=['Young','Middle','Old'])
df['BMI_Squared'] = df['bmi']**2
df['Glucose_Adjusted'] = df['blood_glucose_level']/18.0
df['RiskScore'] = (df['bmi'] + df['blood_glucose_level'] + df['hbA1c_level'])/3

conditions = [
    (df['blood_glucose_level']>140)&(df['bmi']>30),
    (df['blood_glucose_level']>120)
]
choices = ['High','Medium']
df['RiskFlag'] = np.select(conditions, choices, default='Low')

temp = df[['year','RiskFlag']].drop_duplicates()
df = df.merge(temp, on='year', how='left')

end = time.perf_counter()
print(f"Total runtime: {end-start:.8f} seconds")
