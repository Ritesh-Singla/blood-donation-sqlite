import sqlite3
conn= sqlite3.connect("blooddatabase.db")

c=conn.cursor()

 c.execute(""" CREATE TABLE donors(
  		Full_name text,
  		Gender text,
  		Blood_Group text,
  		Address text,
  		Contact integer,
  		City text,
  		State text,
  		Zip_code integer
  						)
  			""")