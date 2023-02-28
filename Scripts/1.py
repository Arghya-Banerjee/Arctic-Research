from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('../Dataset/NSIDC/N_Yearly_SeaIce_Extent_1978_2023.csv')

fig, ax = plt.subplots()
ax.plot(df['Date'], df['Extent'])
plt.show()