# eda-titanic-analysis
Exploratory Data Analysis (EDA) on Titanic Dataset


# 🧪 Exploratory Data Analysis (EDA) on Titanic Dataset

This project presents Exploratory Data Analysis (EDA) performed on the Titanic dataset using Python. The analysis focuses on understanding key patterns and trends in the data through summary statistics and data visualizations.


## 📌 Objective

- Understand the structure and distribution of the Titanic dataset.
- Identify trends, anomalies, and patterns in numerical features.
- Derive insights using summary statistics and visualizations.



## 📂 Dataset

- Dataset: Titanic dataset (commonly used in data science)
   

## 🛠 Tools & Libraries Used

- **Google Colab** – Notebook environment
- **Pandas** – Data manipulation
- **Matplotlib** – Basic visualizations
- **Seaborn** – Statistical visualizations
- **Plotly** – Interactive visualizations (optional)



## 🔍 EDA Steps Performed

1. **Data Loading and Basic Exploration**
   - Viewed first few records, shape, columns, and data types.

2. **Handling Missing Values**
   - Checked for null values.
   - Discussed possible treatments.

3. **Summary Statistics**
   - Used `.describe()`, `.mean()`, `.median()`, `.std()` for numerical features.
   - Focused on key columns: `Age`, `Fare`, `SibSp`, `Parch`.

4. **Univariate Visualizations**
   - Histograms to show the distribution of numerical features.
   - Boxplots to detect outliers and compare distributions.

5. **Bivariate Visualizations**
   - Countplots and boxplots for `Survived` vs features like `Sex`, `Pclass`, `Age`, `Fare`.



## 📈 Sample Visuals

- Histogram and boxplot of `Age`
- Histogram and boxplot of `Fare`
- Countplot of `Survived` by `Sex`
- Boxplot of `Fare` grouped by `Survived`



## 🧠 Key Insights

- Female passengers had a higher survival rate.
- Passengers in 1st class were more likely to survive.
- Younger passengers showed better survival chances.
- Higher fares were often associated with survival.
