import sqlite3
import csv

# Connect to the SQLite3 database
conn = sqlite3.connect(r'C:\Users\manna\OneDrive\Desktop\Data Collection and Analysis\Assignment_Database.db')
cursor = conn.cursor()

# SQL query to extract total quantities of each item bought per customer aged 18-35
sql_query = """
SELECT c.customer_id,
       SUM(CASE WHEN i.item_name = 'x' THEN o.quantity ELSE 0 END) AS Total_x,
       SUM(CASE WHEN i.item_name = 'y' THEN o.quantity ELSE 0 END) AS Total_y,
       SUM(CASE WHEN i.item_name = 'z' THEN o.quantity ELSE 0 END) AS Total_z
FROM orders o
JOIN sales s ON o.sales_id = s.sales_id
JOIN customers c ON s.customer_id = c.customer_id
JOIN items i ON o.item_id = i.item_id
WHERE c.age >= 18 AND c.age <= 35
GROUP BY c.customer_id;
"""

# Execute the SQL query
cursor.execute(sql_query)

# Fetch all the results
results = cursor.fetchall()

# Write results to a CSV file
with open('output_sql.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['CustomerID', 'Total_x', 'Total_y', 'Total_z'])
    writer.writerows(results)

# Close the database connection
conn.close()
