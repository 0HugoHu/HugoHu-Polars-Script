"""CLI interface for ids706_python_template project.
"""

import pandas as pd
import random
import polars as pl
import matplotlib.pyplot as plt

def createNewCSV():
    # Generate random data
    data = {
        "ID": range(1, 10001),  # IDs from 1 to 10000
        "Name": [f"Person_{i}" for i in range(1, 10001)],
        "Age": [random.randint(18, 60) for _ in range(1, 10001)],
        "Salary": [random.randint(30000, 100000) for _ in range(1, 10001)],
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv("large_data.csv", index=False)

    print("Large dataset saved to 'large_data.csv'")
 

def visualizeData():
    # Read the CSV file into a Polars DataFrame
    df = pl.read_csv('large_data.csv')

    # Calculate descriptive statistics
    stats = df.describe()

    # Print the statistics
    print(stats)

    # Visualize the data (e.g., a histogram of ages)
    df.select('Salary').to_pandas().plot(kind='hist', bins=10, rwidth=0.9)
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.title('Histogram of Salary')
    plt.show()
    plt.savefig('plot.png')


def main():

    createNewCSV()

    visualizeData()
