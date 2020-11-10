# imports
from os import curdir
import sqlite3
from sqlite3 import Error
import os
from typing import Tuple
import pandas as pd
from pandas.core.indexing import IndexSlice

# converts the students performance csv file into a format which can be added to sqlite database (list of tuples)
with open('StudentsPerformance.csv','r') as csv_file:
    csv_values = csv_file.read()
    csv_list = csv_values.splitlines() # the csv file is now a list of different rows
    sql_formatted_data = []
    id = 0

    for row in csv_list:
        sql_format_list = []
        list_of_vals = row.split(',')
        for val in list_of_vals:
            val = val.strip('\"')                       # strips away outside quotation marks
            try:
                sql_format_list.append(int(val))        # turns the value into an integer if possible
            except:
                sql_format_list.append(val)             # if it's not a number, adds the string to the list
        sql_format_tuple = tuple(sql_format_list)       # converts the list of clean data into a tuple
        sql_formatted_data.append(sql_format_tuple)     # appends the tuple to the list of sql_formatted_data

# creates a connection to a database
def create_connection(path):
    """ Creates a connection to a SQLite Database """
    connection = None

    # tries a connection first
    try:
        connection = sqlite3.connect(path)
        print("Connection worked!")
    except Error as error:
        print(f'Error: {error}')
    
    # returns the connection object
    return connection

# executes a single sql query
def execute_query(connection, query):
    """executes a single sql command"""
    cursor = connection.cursor()

    try:
        cursor.execute(query)   # runs the commands
        connection.commit()     # saves the database
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# defines path to sqlite database and creates the connection
curdir = os.getcwd()
connection = create_connection(f'{curdir}/student_performance.sqlite')
cursor = connection.cursor()

# prints out the table heads for reference
for title in sql_formatted_data[0]:
    print(title)

# sql command to create table
create_table = """
    CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY,
    gender TEXT NOT NULL,
    race_ethnicity TEXT NOT NULL,
    parental_level_of_education TEXT NOT NULL,
    lunch TEXT NOT NULL,
    test_preparation_course TEXT NOT NULL,
    math_score INTEGER NOT NULL,
    reading_score INTEGER NOT NULL,
    writing_score INTEGER NOT NULL
);
"""
# creates the table in the database
execute_query(connection, create_table)

connection.executemany("INSERT INTO Students (gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, math_score, reading_score, writing_score) values (?,?,?,?,?,?,?,?)", sql_formatted_data[1:])

# turns the SQL Database into a Pandas Dataframe
print("\n - - - - - - PANDAS PART HERE - - - - - - - ")
df = pd.read_sql_query("SELECT * FROM Students WHERE math_score > 70",connection)
print(df)

