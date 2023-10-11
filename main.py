import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data for 100 individuals
n = 100
bmi = np.random.uniform(18, 35, n)  # BMI ranges roughly from 18 to 35
blood_pressure = np.random.uniform(70, 160, n)  # Blood pressure ranges roughly from 70 to 160

# Adding some random noise to create a simulated correlation
blood_pressure += bmi * 2.5 + np.random.normal(0, 10, n)

# Create a DataFrame
df = pd.DataFrame({'BMI': bmi, 'Blood_Pressure': blood_pressure})

df.head()


# Plotting the data
plt.figure(figsize=(10, 6))
sns.scatterplot(x='BMI', y='Blood_Pressure', data=df)
plt.title('Scatter Plot of BMI vs Blood Pressure')
plt.xlabel('Body Mass Index (BMI)')
plt.ylabel('Blood Pressure')
plt.show()


