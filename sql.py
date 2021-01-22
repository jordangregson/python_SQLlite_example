import sqlite3
import os
os.system("clear")

from employee import Employee

# # Create a database from memory
# conn = sqlite3.connect(':memory:')

# Create a database file
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", (emp.first, emp.last, emp.pay))

def get_emps_by_name(lastname):
    
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                    {'first': emp.first, 'last': emp.last, 'pay': pay})
                    

def remove_emp (emp):
    c.execute("DELETE from employees WHERE first = :first AND last = :last",
                {'first': emp.first, 'last': emp.last})

emp_1 = Employee('Jordan', 'Gregson', 500)
emp_2 = Employee('Theo', 'Gregson', 50)

insert_emp(emp_1)
insert_emp(emp_2)

update_pay(emp_2, 95000)


emps = get_emps_by_name('Gregson')
print(emps)

# # INCORRECT WAY TO DO THIS

# # c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))

# # # One way to do this
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

# conn.commit

# # c.execute("SELECT * FROM employees WHERE last='Gregson'")

# # # Another way to do this
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first' : emp_2.first, 'last' : emp_2.last, 'pay' : emp_2.pay})

# conn.commit

# c.execute("SELECT * FROM employees WHERE last='Gregson'")

# # Search for a certain name
# # c.execute("SELECT * FROM employees WHERE last=?", ('Gregson',))


# # c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Gregson',})

# print(c.fetchall())

# conn.commit()

conn.close()
