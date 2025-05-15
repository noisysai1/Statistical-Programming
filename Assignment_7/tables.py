print("DATA-51100, FALL-2023")
print("Sai Kumar Murarishetti")
print("PROGRAMMING ASSIGNMENT #7")
print()

# Importing libraries
import pandas as pd
import numpy as np

## Read data, prepare display
# Read the data from the 'ss13hil.csv' file into a DataFrame called 'df'
df = pd.read_csv('ss13hil.csv', header=0, skip_blank_lines=True)

# Set options for displaying DataFrame
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:.6f}'.format)
# Function to generate Table 1 - Descriptive Statistics of HINCP, grouped by HHT - Household/family type
def tb1(df):
    """
    Table 1 - Descriptive Statistics of HINCP, grouped by HHT - Household/family type
    """
    # Rename column HHT to 'HHT - Household/family type'
    df = df.rename(columns={'HHT': 'HHT - Household/family type'})

    # Mapping values in HHT column to descriptive strings
    household_types = {
        1: 'Married couple household',
        2: 'Other family household:Male householder, no wife present',
        3: 'Other family household:Female householder, no husband present',
        4: 'Nonfamily household:Male householder:Living alone',
        5: 'Nonfamily household:Male householder:Not living alone',
        6: 'Nonfamily household:Female householder:Living alone',
        7: 'Nonfamily household:Female householder:Not living alone'
    }
    df['HHT - Household/family type'] = df['HHT - Household/family type'].replace(household_types)

    # Grouping by HHT column and calculating descriptive statistics for HINCP
    table1 = df['HINCP'].groupby(df['HHT - Household/family type']).describe()[['mean', 'std', 'count', 'min', 'max']]

    # Sorting with mean value in descending order
    table1 = table1.sort_values('mean', ascending=False)

    # Cast count, min, and max columns to integer type
    table1 = table1.astype({"count": "int", "min": "int", "max": "int"})

    # Printing the table1
    print("*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***")
    print(table1)

# Function to generate Table 2 - HHL vs. ACCESS - Frequency Table
def tb2(df):
    """
    This function generates Table 2 - HHL vs. ACCESS - Frequency Table
    """
    # Selecting only required columns
    table2 = df.loc[:, ['HHL', 'ACCESS', 'WGTP']]

    # Dropping rows who have na
    table2 = table2.dropna()

    # Renaming columns
    table2.columns = table2.columns.str.replace('HHL', 'HHL-Household Language')

    # Map language labels
    labels = ["English only", "Spanish", "Other Indo-European languages", "Asian and Pacific Island languages",
              "Other language", "All"]
    s = dict(zip(range(1, 6), labels))
    table2['HHL-Household Language'] = table2['HHL-Household Language'].replace(s)

    # Map access labels
    p = {1.0: 'Yes w/ Subsrc.', 2.0: 'Yes wo/ Subsrc.', 3.0: 'No'}
    table2['ACCESS'] = table2['ACCESS'].replace(p)

    # Group by language and access, sum weights
    table2 = table2.groupby(['HHL-Household Language', 'ACCESS'], as_index='labels', sort=False,
                            group_keys=True).agg(
        {'WGTP': 'sum'})

    # Compute percentage table
    table2 = table2.groupby(level=0, group_keys=False).apply(lambda x: 100 * x / table2['WGTP'].sum()).unstack(
        'ACCESS')

    # Reorder columns
    table2 = table2[[('WGTP', 'Yes w/ Subsrc.'), ('WGTP', 'Yes wo/ Subsrc.'), ('WGTP', 'No')]]

    # Sort by 'Yes w/ Subsrc.'
    table2 = table2.sort_values(('WGTP', 'Yes w/ Subsrc.'), ascending=False)

    # Add row and column totals
    table2['WGTP', '  All'] = table2.sum(numeric_only=True, axis=1)
    table2.loc['All'] = table2.sum(numeric_only=True, axis=0)

    # Format as percentage strings
#    table2 = table2.applymap(lambda x: "{:0.02%}".format(x / 100))
    table2 = table2.apply(lambda x: x.map(lambda val: "{:0.02%}".format(val / 100)))
    # Printing the table2
    print("*** Table 2 - HHL vs. ACCESS - Frequency Table ***")
    print(table2)

# Function to generate Table 3 - Quantile Analysis of HINCP - Household income (past 12 months)

def tb3(df):
    """
    This function generates Table 3 - Quantile Analysis of HINCP - Household income (past 12 months)
    """
    temp_df1 = pd.qcut(df["HINCP"], q=3, labels=['low', 'medium', 'high'])
    temp_df2 = df["HINCP"].groupby(temp_df1, observed=False)
    k = temp_df2.describe()[["min", "max", "mean"]]
    df3 = df["WGTP"].groupby(temp_df1, observed=True)
    df3 = df["WGTP"].groupby(temp_df1,observed=True)
    df3 = pd.DataFrame(df3)
    df3 = np.array(df3)
    hhc = []
    for i in range(0, 3):
        hhc.append(df3[i][1].sum())
    k["household_count"] = hhc
    # changing required data type of the output format
    k = k.astype({"min": "int", "max": "int"})

    # Printing the table1
    print("*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***")
    print(k)
# Call functions to generate tables and display them
tb1(df)
print()
tb2(df)
print()
tb3(df)