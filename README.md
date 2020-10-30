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
