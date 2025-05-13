
# Week 6 Assignment
#print("DATA-51100, FALL-2023")
#print("Sai Kumar Murarishetti")
#print("PROGRAMMING ASSIGNMENT #6")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from the 'ss13hil.csv' file into a Pandas DataFrame
data = pd.read_csv('ss13hil.csv')

# Create a figure to place the subplots
fig = plt.figure(figsize=[15, 10], facecolor='white')
fig.suptitle('Sample Output', y=1.02, fontweight="bold")

# ==================================== Pie chart on the number of household languages ======================================

# Create the first subplot for the pie chart
ax1 = fig.add_subplot(2, 2, 1)

# Extract the 'HHL' (Household Language) column and fill missing values with 1
HHL_df = data[['HHL']]
HHL_df = HHL_df.assign(HHL=HHL_df['HHL'].fillna(1))

# Define labels for the pie chart
hhl_labels = ['English Only', 'Spanish', 'Other Indo-European', 'Asian and Pacific Island language', 'Other']

# Count the occurrences of each language and plot a pie chart
hhl = HHL_df.HHL.value_counts()
ax1.axis('equal')
ax1.pie(hhl, startangle=240)
ax1.legend(hhl_labels, loc='upper left', prop={'size': 6})
ax1.set_title('Household Languages')  # Setting a title for the plot

# ====================================== Histogram on household income ================================================

# Create the second subplot for the histogram
ax2 = fig.add_subplot(2, 2, 2)

# Extract the 'HINCP' (Household Income) column
hincp = data["HINCP"]

# Plot a kernel density estimate (KDE) line
hincp.plot(kind='kde', color='black', ls='dashed')

# Clean up the data by setting values less than 1 to 1 and filling NaN values with 1
data.loc[data.HINCP < 1, "HINCP"] = 1
hincp = hincp.fillna(1)

# Create logarithmically spaced bins for the histogram
logbin = np.logspace(1, 7, num=100)

# Plot a histogram with log-scaled x-axis
ax2.hist(hincp, bins=logbin, facecolor='g', alpha=0.5, histtype='bar', density=True, range=(0, len(data['HINCP'])))
ax2.set_xscale('log')
ax2.set_title("Distribution of Household income", size="small")
ax2.set_xlabel("Household Income($)-Log Scaled", size="small")
ax2.set_ylabel("Density", size="small")

# Define custom y-tick values and labels for better readability
h_vals = np.arange(0, 0.000025, step=0.000005)
ax2.set_yticks(h_vals)
ax2.set_yticklabels(['{:,.6f}'.format(x) for x in h_vals], fontsize="small")
ax2.grid(color='gray', linestyle='-', linewidth=1, alpha=0.2)

# ================================== Bar chart on thousands of households for each VEH ====================================

# Create the third subplot for the bar chart
ax3 = fig.add_subplot(2, 2, 3)

# Extract the 'VEH' (Number of Vehicles) column and remove NaN values
veh_data = data['VEH'].dropna()

# Calculate the number of households for each number of vehicles and adjust for readability
veh_count = list(data.groupby('VEH').size() / 10)

# Define values for the x-axis
values = list(range(0, 7))

# Create a bar chart
plt.bar(values, veh_count, color='red')
plt.xlabel('# of Vehicles', size='medium')  # Setting x label
plt.ylabel('Thousands of Households', size='medium')  # Setting y label
plt.title("Vehicles available in Households")  # Setting title

# ==================================== Scatter plot on TAXP vs. VALP ================================================

# Create the fourth subplot for the scatter plot
ax4 = fig.add_subplot(2, 2, 4)

# Create series from data values for 'VALP' (Property Values) and 'TAXP' (Property Taxes)
valp = pd.Series(data['VALP'])
taxp = pd.Series(data['TAXP']).replace({
    1: 0, 2: 1, 3: 50, 4: 100, 5: 150, 6: 200, 7: 250, 8: 300, 9: 350, 10: 400, 11: 450, 12: 500, 13: 550, 14: 600,
    15: 650, 16: 700, 17: 750, 18: 800, 19: 850, 20: 900, 21: 950, 22: 1000, 23: 1100, 24: 1200, 25: 1300, 26: 1400,
    27: 1500, 28: 1600, 29: 1700, 30: 1800, 31: 1900, 32: 2000, 33: 2100, 34: 2200, 35: 2300, 36: 2400, 37: 2500,
    38: 2600, 39: 2700, 40: 2800, 41: 2900, 42: 3000, 43: 3100, 44: 3200, 45: 3300, 46: 3400, 47: 3500, 48: 3600,
    49: 3700, 50: 3800, 51: 3900, 52: 4000, 53: 4100, 54: 4200, 55: 4300, 56: 4400, 57: 4500, 58: 4600, 59: 4700,
    60: 4800, 61: 4900, 62: 5000, 63: 5500, 64: 6000, 65: 7000, 66: 8000, 67: 9000, 68: 10000
})

# Create a scatter plot with color-coding based on 'MRGP' and adjusting point size based on 'WGTP'
plt.scatter(valp, taxp, marker='o', s=data['WGTP'] / 5, c=data['MRGP'], cmap='seismic', vmax=5000, alpha=0.20)


#Set ticks and tick labels for both axix
x_val_ax4 = np.arange(0, 1200000, step = 200000)
ax4.ticklabel_format(useOffset=False, style='plain')
ax4.set_xlim(0, 1200000)
ax4.set_ylim(0, 10800)
ax4.set_yticks([0, 2000, 4000, 6000, 8000, 10000])
ax4.set_yticklabels(['0', '2000', '4000', '6000', '8000', '10000'], fontsize='medium')
# Set lables and title
ax4.set_title('Property Taxes vs Property Values')
ax4.set_xlabel('Property Value ($)', size = 'medium')
ax4.set_ylabel('Taxes ($)', size = 'medium')
# Using colorbar
colorbar=plt.colorbar()
colorbar.ax.tick_params(labelsize=8)
colorbar.ax.set_ylabel('First Mortgage Payment (Monthly $)', size = 'medium', rotation=90)#, horizontalalignment='right')
plt.xlabel("Property Value($)")
plt.ylabel("Taxes($)")
plt.title("Property Taxes vs Property Values")

plt.tight_layout()
plt.savefig('pums.png', dpi = 400, bbox_inches = 'tight')