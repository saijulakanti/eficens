import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Walmart.csv")
print(df.columns)
#sns.pairplot(df, hue="Store")

sns.relplot(
    data=df,
    x="Store", y="Unemployment", col="Date",
    hue="Holiday_Flag", style="Holiday_Flag", size="Fuel_Price",
)


plt.show()
