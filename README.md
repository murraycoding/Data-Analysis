# SQL Notes

Relational Database Management System (RDMS)
## Database basics

### What is a database?
Any collection of related information. Databases can also be stored in different way. Database design can vary depending the needs of the database and how the data needs to be accessed. Each database is broken up into smaller sections called fields. A field within a database is a column which is designed to hold the same specific information. For example, within a student database, there may be fields for first name, last name, age, grade and gender.

## Main database commands
While SQL (Structured Query Language) is relatively standard, there are some slight variations. However, within the variations there are 5 main commands which must remain relatively the same.

### SELECT

### UPDATE

### DELETE

### INSERT

### WHERE

## Database Commands
Above are the 5 main commands but there are more that are the most commonly used database commands. Below are the most commonly used SQL Query Commands and what they do.

**SELECT**: extracts data from a database
**UPDATE**: updates data in a database
**DELETE**: deletes data from a database
**INSERT INTO**: inserts new data into a database
**CREATE DATABASE**: creates a new database
**ALTER DATABASE**: modifies a database
**CREATE TABLE**: creates a new table
**ALTER TABLE**: modifies a table
**DROP TABLE**: deletes a table
**CREATE INDEX**: creates an index (search key)
**DROP INDEX**: deletes an index

### SELECT 
The SELECT command is used to select different fields from a database. You can specify the fields you would like to select by separating them with commas or type the * symbol to select all from the database.

    Put in an example once all of the notes are typed
    
### FROM
The FROM command is used to tell which database you would like to get the specified fields from
    
### SELECT DISTINCT
The SELECT DISTINCT command is used to do exactly what it sounds like, it will return rows with distinct data.

    Put in an example once all of the notes are typed

### COUNT
The COUNT command simply returns the number of rows which all within the query.

### WHERE
The WHERE command comes after the FROM command to specify the condition on which you want to pull the data.

### AND, OR, NOT
In SQL, commands are not case sensitive but it is common practice to make them in ALL CAPS to differentiate the commands from the data bases and fields the commands are trying to access.



# SQL Lite
SQL Lite is the most straightforward database system in Python since it is already built in to Python by default. It is also serverless and self-contained so it just reads and writes to a file. Below is example code to establish a connection with a SQLite database locally.

    # Example file for the SQLite database

    from os import curdir
    import sqlite3
    from sqlite3 import Error
    import os

    def create_connection(path):
        connection = None

      try:
          connection = sqlite3.connect(path)
          print("Connection to SQLite DB successful")
      except Error as e:
          print(f"The error '{e}' occurred")

      return connection

    # gets the 'current working directory' (CWD)
    curdir = os.getcwd()
    print(curdir)

    # sets up and establishes connection with CWD
    connection = create_connection(f'{curdir}/sm_app.sqlite')
