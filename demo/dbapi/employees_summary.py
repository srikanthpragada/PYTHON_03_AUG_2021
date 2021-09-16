# Display count of employees and average salary

import sqlite3
import dbutil

try:
    con = sqlite3.connect(dbutil.DBNAME)
    cur = con.cursor()
    cur.execute("select count(*), avg(salary) , sum(salary) from employees")  # SQL Command
    count, avg, total = cur.fetchone()
    print(f"Count   : {count:10}")
    print(f"Average : {avg:10.0f}")
    print(f"Total   : {total:10.0f}")
    cur.close()
    con.close()
except Exception as ex:
    print('Error :', ex)
