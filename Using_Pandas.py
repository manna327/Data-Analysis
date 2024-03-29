import pandas as pd
import sqlite3

# Connect to the SQLite3 database
conn = sqlite3.connect(r'C:\Users\manna\OneDrive\Desktop\Data Collection and Analysis\Assignment_Database.db')

# SQL query to extract data
sql_query = """
SELECT c.customer_id, i.item_name, SUM(o.quantity) AS Total
FROM orders o
JOIN sales s ON o.sales_id = s.sales_id
JOIN customers c ON s.customer_id = c.customer_id
JOIN items i ON o.item_id = i.item_id
WHERE c.age >= 18 AND c.age <= 35
GROUP BY c.customer_id, i.item_name;
"""

# Read data into a DataFrame using pandas
df = pd.read_sql_query(sql_query, conn)

# Pivot the DataFrame to get total quantities for each item per customer
df_pivot = df.pivot(index='customer_id', columns='item_name', values='Total').fillna(0)

# Filter out customers who didn't buy anything
df_pivot = df_pivot[(df_pivot.sum(axis=1) != 0)]

# Write the DataFrame to a CSV file
df_pivot.to_csv('output_pandas.csv', sep=';', index=True)

# Close the database connection
conn.close()
