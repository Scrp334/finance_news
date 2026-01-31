import seaborn as sns
import matplotlib.pyplot as plt

# Testing for corr_matrix as 5*5 matrix correlation matrix
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True,cmap='coolwarm', fmt=".2f")
plt.title('Asset Correlation Matrix: Why We Diversified')
plt.show
