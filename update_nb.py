import nbformat as nbf

nb = nbf.v4.new_notebook()

code_imports = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
"""

code_class = """class BigMartAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("Data loaded successfully.")

    def preprocess(self):
        self.df['Item_Weight'] = self.df['Item_Weight'].fillna(self.df['Item_Weight'].mean())
        self.df['Item_Visibility'] = self.df['Item_Visibility'].replace(0, np.nan)
        self.df['Item_Visibility'] = self.df['Item_Visibility'].fillna(self.df['Item_Visibility'].mean())
        print("Preprocessing completed.")

    def calculate_age(self):
        CURRENT_YEAR = 2026
        self.df['Outlet_Age'] = CURRENT_YEAR - self.df['Outlet_Establishment_Year']
        print("Outlet Age calculated.")

    def remove_outliers(self):
        Q1 = self.df['Item_Outlet_Sales'].quantile(0.25)
        Q3 = self.df['Item_Outlet_Sales'].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        self.df = self.df[(self.df['Item_Outlet_Sales'] >= lower) & (self.df['Item_Outlet_Sales'] <= upper)]
        print("Outliers removed.")

    def data_normalizer(self):
        self.df['Normalized_Sales'] = (
            (self.df['Item_Outlet_Sales'] - np.mean(self.df['Item_Outlet_Sales'])) /
            np.std(self.df['Item_Outlet_Sales'])
        )
        self.df['Rolling_Sales'] = self.df['Item_Outlet_Sales'].rolling(5).mean()
        print("Data normalized.")

    def analyze_sales(self):
        avg_sales = self.df.groupby(['Outlet_Identifier', 'Item_Identifier'])['Item_Outlet_Sales'].mean()
        print("Average Sales Head:\\n", avg_sales.head())
        
        size_map = {'Small': 1000, 'Medium': 2000, 'High': 3000}
        self.df['Size_Value'] = self.df['Outlet_Size'].map(size_map)
        self.df['Sales_Density'] = self.df['Item_Outlet_Sales'] / self.df['Size_Value']

        size_perf = self.df.groupby('Outlet_Size')['Item_Outlet_Sales'].mean()
        type_perf = self.df.groupby('Outlet_Type')['Item_Outlet_Sales'].mean()
        self.df['Age_Group'] = pd.cut(self.df['Outlet_Age'], bins=3)
        age_perf = self.df.groupby('Age_Group', observed=False)['Item_Outlet_Sales'].mean()
        print("\\nSize Performance:\\n", size_perf)
        print("\\nType Performance:\\n", type_perf)
        print("\\nAge Performance:\\n", age_perf)

    def find_underperforming(self):
        outlet_sales = self.df.groupby('Outlet_Identifier')['Item_Outlet_Sales'].mean()
        threshold = outlet_sales.mean()
        underperforming = outlet_sales[outlet_sales < threshold]
        print("Underperforming Outlets:\\n", underperforming)

    def plot_bar(self):
        size_sales = self.df.groupby('Outlet_Size')['Item_Outlet_Sales'].mean()
        plt.figure(figsize=(8,5))
        plt.bar(size_sales.index, size_sales.values, color='skyblue')
        plt.title("Outlet Size vs Avg Sales")
        plt.xlabel("Outlet Size")
        plt.ylabel("Sales")
        plt.show()

    def plot_heatmap(self):
        heatmap_data = self.df.pivot_table(
            values='Item_Outlet_Sales',
            index='Outlet_Size',
            columns='Outlet_Identifier',
            aggfunc='mean'
        )
        plt.figure(figsize=(10,6))
        sns.heatmap(
            heatmap_data,
            annot=True,
            fmt='.1f',
            cmap='coolwarm',
            linewidths=.5,
        )
        plt.title('Outlet Size and Identifier Heatmap')
        plt.show()"""

code_execution = """# Execution
file_path = "C:/Users/ACER/Downloads/BigMart Sales.csv"
analyzer = BigMartAnalyzer(file_path)

analyzer.load_data()
analyzer.preprocess()
analyzer.calculate_age()
analyzer.remove_outliers()
analyzer.data_normalizer()
analyzer.analyze_sales()
analyzer.find_underperforming()
analyzer.plot_bar()
analyzer.plot_heatmap()"""

nb['cells'] = [
    nbf.v4.new_markdown_cell('# BigMart Sales Data Analyzer'),
    nbf.v4.new_code_cell(code_imports),
    nbf.v4.new_markdown_cell('## Analyzer Class Definition'),
    nbf.v4.new_code_cell(code_class),
    nbf.v4.new_markdown_cell('## Execution Block'),
    nbf.v4.new_code_cell(code_execution)
]

with open('E:/Bl_Python_Training/Data_Handling/Test.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print("Saved transformed notebook.")
