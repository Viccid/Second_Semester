import psycopg2   # Postgres Connector
import csv


# import mysql.connector  # Assuming you are using MySQL

# This establish connection to the database
connection = psycopg2.connect(
    user = "livedata",
    host = "localhost",
    port = "5432",
    database = "composedata",
    password="success1"
)

cursor = connection.cursor()

with open( 'sample_data.csv', 'r') as csvfile:   # Open the CSV file for reading
    reader = csv.DictReader(csvfile)             # Create a CSV reader object
    
    # Iterate over each row in the CSV file
    for row in reader:

         # Execute SQL query to insert data into the database
        cursor.execute(                                                                     
            "INSERT INTO students (name, email, phone_number, address) VALUES(%s, %s, %s, %s)",
            (row['name'], row['email'], row['phone_number'], row['address'])
        )
       
    connection.commit()    # Commit the transaction
    cursor.close()
    connection.close()     # Close the cursor and connection