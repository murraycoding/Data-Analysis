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

    Put in an example once all of the notes are typed

### WHERE
The WHERE command comes after the FROM command to specify the condition on which you want to pull the data.

    Put in an example once all of the notes are typed

### AND, OR, NOT
The AND, OR and NOT commands are used to combine different conditions in the WHERE command.

    Put in an example once all of the notes are typed
    
### ORDER BY
The ORDER BY command is used to order the data after it is pulled with the FROM command. If you would like to order the data by multiple fields, you can do so by putting the field after the ORDER BY command with commas separating each.

    Put in an example once all of the notes are typed
    
### INSERT INTO
The INSERT INTO command is used to insert the data into a table. The insert into command can be written in two differnt ways. The first specifies which columns the data values will go into. The other version of the command does not specify which columns the data will go into. In the later case, the command will assume you have the correct number of values to fill every field into the table.

    Put in an example once all of the notes are typed
    
### NULL
A field will a NULL value is a field with no value. Keep in mind that a NULL value is distinctly different than one with a zero value or one with spaces. Using the WHERE command, you can check for null values. The example below shows ... (descrie example below)

    Put in an example once all of the notes are typed
    
### UPDATE
The UPDATE command is used to change records in a database. Using the SET command, you can specify what the new values will be. The WHERE command is also important here to specify what exact values should be updated. If you do not include the WHERE command, the program will update all values within the given range.

    Put in an example once all of the notes are typed
    
### DELETE
The DELETE command is used to delete records from a database. This should be used with the FROM and WHERE commands to tell the program which database should be deleted from and what conditions need to be met in order to delete the records. If no WHERE command is given then all records from the data will be deleted.

    Put in an example once all of the notes are typed

### SELECT TOP
The SELECT TOP command selects the top rows (of a given number) of the database. Similar to other statements, you can use the WHERE command to narrow the database down before selecting the data. You can also combine this with the ORDER BY command to get the top results in a certain field.

In SQL, commands are not case sensitive but it is common practice to make them in ALL CAPS to differentiate the commands from the data bases and fields the commands are trying to access.

    Put in an example once all of the notes are typed
    
### MIN / MAX
The MIN and MAX commands combined with the SELECT command will select the largest or smallest data within the database.

    Put in an example once all of the notes are typed
    
### COUNT / SUM / AVG
The commands COUNT, SUM, and AVG can be used with the SELECT command to determine the count, the sum or the average of a set of data. The count data can count the number of rows of string data. However, SUM and AVG are required to have numerical data in order to function properly.

    Put in an example once all of the notes are typed
    
### LIKE
The LIEK command will search string data and return values which are "like" the given search criteria. Using special commands, you can specify how you want to search for information. For a full list on the different patters you can use, click [here](https://www.w3schools.com/sql/sql_like.asp)


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
