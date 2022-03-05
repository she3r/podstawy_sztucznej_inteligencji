# Import Seaborn and Matplotlib
import seaborn as sns
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a violin plot using Seaborn
sns.violinplot(x="day", y="total_bill", hue="time", data=tips)

# Display the plot
plt.show()