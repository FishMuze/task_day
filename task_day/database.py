import sqlite3

con = sqlite3.connect("amba.db")
print("Database opened successfully")

con.execute("create table ambassador(Date text DEFAULT  CURRENT_TIMESTAMP,amba integer NOT NULL, queue_id integer NOT NULL, state integer NOT NULL,amount integer NOT NULL, reason  TEXT NOT NULL, task_counter integer NOT NULL)")

print("Table create Successfully")

con.close()