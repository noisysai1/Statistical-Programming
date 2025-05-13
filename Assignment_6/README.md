Name: Sai Kumar Murarishetti
Assignment #6
Course: DATA-51100 – Statistical Programming

🧾 Description
The vispums.py script uses PUMS (Public Use Microdata Sample) data from the ss13hil.csv dataset to generate four key visualizations that explore various aspects of household data:

🔹 Visualizations Included:

Pie Chart – Distribution of Household Languages (HHL)

Histogram + KDE – Distribution of Household Incomes (HINCP) using log scale

Bar Chart – Number of Vehicles Available per Household (VEH)

Scatter Plot – Property Taxes (TAXP) vs Property Values (VALP) with color coded by Mortgage Payments (MRGP) and size by Weight (WGTP)

📦 Dependencies
The script uses the following Python libraries:

pandas
numpy
matplotlib

To install them:

pip install pandas numpy matplotlib

The final visualization is saved as an image file:

📄 pums.png – Contains all four plots arranged in a 2x2 subplot layout.

📊 Dataset

The script assumes access to the ss13hil.csv dataset (2013 ACS Housing Microdata Sample). Ensure this file is in the same directory as vispums.py.

▶️ How to Run

python vispums.py
