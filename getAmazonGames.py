"""
Author: lokihellfire2008
GitHub URL: https://github.com/lokihellfire2008/GameLibrary
"""

import sqlite3
import csv
import os

# Get the current user's username
current_user = os.getlogin()

# Define the path to the SQLite database
database_path = f"C:\\Users\\{current_user}\\AppData\\Local\\Amazon Games\\Data\\Games\\Sql\\GameProductInfo.sqlite"
print(f"Path: {database_path}")

# Define the query to extract the ProductTitle column from the DbSet table
query = "SELECT ProductTitle FROM DbSet"
print(f"Query: {query}")

# Connect to the SQLite database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Execute the query and fetch all results
cursor.execute(query)
results = cursor.fetchall()

# Define the path to the CSV file
csv_path = f"C:\\Users\\{current_user}\\Desktop\\ProductTitles.csv"

# Write the results to a CSV file
with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["ProductTitle"])  # Write the header
    writer.writerows(results)  # Write the data

# Close the database connection
conn.close()

print(f"Results have been exported to {csv_path}")