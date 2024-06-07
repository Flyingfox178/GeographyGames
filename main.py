import sqlite3
import os

c = sqlite3.connect("terra.db")
#cursor = c.cursor()
#
#files = os.listdir("mondial_sqlite/sql/data")
#for file in files:
#    #commands = [cmd for cmd in open(f"mondial_sqlite/sql/data/{file}").read().replace("\n", " ").split(";")]
#    #for cmd in commands:
#    #    print(cmd)
#    #    cursor.execute(cmd)
#    with open(f"mondial_sqlite/sql/data/{file}", "r") as sql_file:
#        sql_script = sql_file.read()
#    print(sql_script)
#    print(file)
#    cursor.executescript(sql_script)
#
#cursor.close()

cursorNew = c.cursor()

cursorNew.execute("SELECT * FROM Desert")
a = cursorNew.fetchall()
print(a)