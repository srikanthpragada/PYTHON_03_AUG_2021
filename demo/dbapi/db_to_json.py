# Convert Employees table to JSON

import sqlite3
import json
import dbutil


# Converts tuple with emp details to dict
def emp_to_dict(emp):
    return {"id": emp[0], "name": emp[1], "job": emp[2], "salary": emp[3]}


employees = []
con = sqlite3.connect(dbutil.DBNAME)
cur = con.cursor()
cur.execute("select * from employees")  # SQL Command

for emp in cur.fetchall():
    employees.append(emp_to_dict(emp))

cur.close()
con.close()

print(json.dumps(employees))

# Write to file
f = open("employees.json", "wt")
json.dump(employees, f)
f.close()
