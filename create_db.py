import mysql.connector as mycon

# Connect to MySQL server (without specifying the database)
con = mycon.connect(host='localhost', user='root', password="Yeshu@2004")
cur = con.cursor()

# Create the database if it doesn't exist
cur.execute("CREATE DATABASE IF NOT EXISTS Parking")
cur.execute("USE Parking")

# Create the table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS TEST6 (
    V_No varchar(30) not null,
    Name varchar(20),
    V_Type varchar(20),
    Charged int,
    Timing datetime primary key,
    Status varchar(5) default 'in',
    Out_time datetime
)
""")

# Commit changes and close the connection
con.commit()
cur.close()
con.close()

print("Database and table created successfully!")