import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("Titanic dataset.csv")

# Show the first 5 rows
df.head()

# Data types and non-null info
df.info()

# Summary statistics
df.describe()

# Count of null values
df.isnull().sum()

# # Fill missing 'Age' values with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing 'Embarked' values with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop 'Cabin' column due to many nulls
df.drop(columns=['Cabin'], inplace=True)

# Convert 'Sex' to numerical (Label Encoding)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# One-hot encode 'Embarked' column
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Standardize Age and Fare
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Visualize outliers with boxplot
plt.figure(figsize=(10,4))
sns.boxplot(x=df['Age'])
plt.title("Boxplot - Age")
plt.show()

# Remove outliers in 'Age' using IQR
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Age'] >= Q1 - 1.5 * IQR) & (df['Age'] <= Q3 + 1.5 * IQR)]

