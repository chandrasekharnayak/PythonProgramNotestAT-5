import pyodbc

# Connection parameters
dsn = "orclXDB"
user = "system"
password = "godisbest"


# Create a connection
connection_string = f"DSN={dsn};UID={user};PWD={password}"
connection = pyodbc.connect(connection_string)

# Create a cursor
cursor = connection.cursor()

# Example query
query = "SELECT * FROM Authors"
cursor.execute(query)

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
