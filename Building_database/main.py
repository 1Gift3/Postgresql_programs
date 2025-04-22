import psycopg2

def create_table():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Sindiso2017",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("create table students(student_id serial primary key, name text, address text, age integer, number text);")
    print("Student table")
    conn.commit()
    conn.close()

def insert_data():
    # Coding to accept data from user
    name = input("Enter name:")
    address = input("Enter address: ")
    age = input("Enter age: ")
    number = input( "ENter number: ")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Sindiso2017",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("insert into students(name,address,age,number) values(%s, %s,%s,%s)", (name,address,age,number))
    print("data inserted in student table")
    conn.commit()
    conn.close()

insert_data()

# WHAT
# import allows python code to inteact with Postgresql database sending commands getting data back etc
# create table() : connnects to a local Postgre database named studentdb
# - crates a table called students with fields
# - This only defines the functions but calls not the code
# function insert_data(): prompts the user for student details, inserts that data into students and commits and close the connection
# And insert_data() function : runs the script.



