# =====================================================

# ALL-IN-ONE PYTHON PROGRAM

# Covers:

# Functional Programming + Comprehensions +

# Backend Data Transformations + File I/O

# =====================================================
 
from functools import reduce

import json

import csv

from itertools import groupby
 
# -----------------------------------------------------

# SAMPLE BACKEND DATA (could be DB/API response)

# -----------------------------------------------------

employees = [

    {"id": 1, "name": "Raj", "dept": "IT", "salary": 60000},

    {"id": 2, "name": "Anu", "dept": "HR", "salary": 45000},

    {"id": 3, "name": "Kumar", "dept": "IT", "salary": 75000},

    {"id": 4, "name": "Divya", "dept": "Finance", "salary": 50000},

    {"id": 5, "name": "Siva", "dept": "HR", "salary": 55000},

]
 
# =====================================================

# 1️⃣ FUNCTIONAL PROGRAMMING TOOLS

# =====================================================
 
# --- filter(): get employees with salary > 50000

high_salary = list(filter(lambda e: e["salary"] > 50000, employees))
 
# --- map(): extract salaries

salaries = list(map(lambda e: e["salary"], employees))
 
# --- reduce(): total salary

total_salary = reduce(lambda a, b: a + b, salaries)
 
# =====================================================

# 2️⃣ PYTHONIC COMPREHENSIONS

# =====================================================
 
# --- List comprehension: names of IT employees

it_names = [e["name"] for e in employees if e["dept"] == "IT"]
 
# --- Dict comprehension: name -> salary

salary_dict = {e["name"]: e["salary"] for e in employees}
 
# --- Nested comprehension: salary matrix (for demo)

salary_matrix = [[e["name"], e["salary"]] for e in employees]
 
# =====================================================

# 3️⃣ BACKEND DATA TRANSFORMATION PIPELINE

# Sorting → Grouping → Processing

# =====================================================
 
# --- Sorting by department

employees_sorted = sorted(employees, key=lambda e: e["dept"])
 
# --- Grouping by department

grouped_by_dept = {}

for dept, group in groupby(employees_sorted, key=lambda e: e["dept"]):

    grouped_by_dept[dept] = list(group)
 
# --- Pipeline: Filter → Map → Sort

pipeline_result = sorted(

    map(lambda e: e["name"],

        filter(lambda e: e["salary"] >= 50000, employees))

)
 
# =====================================================

# 4️⃣ FILE I/O BASICS

# =====================================================
 
# -------- TXT FILE --------

with open("employees.txt", "w") as f:

    for e in employees:

        f.write(f"{e['id']} {e['name']} {e['dept']} {e['salary']}\n")
 
# -------- JSON FILE --------

with open("employees.json", "w") as f:

    json.dump(employees, f, indent=4)
 
# -------- CSV FILE --------

with open("employees.csv", "w", newline="") as f:

    writer = csv.DictWriter(f, fieldnames=["id", "name", "dept", "salary"])

    writer.writeheader()

    writer.writerows(employees)
 
# =====================================================

# OUTPUT SECTION

# =====================================================

print("High Salary Employees:", high_salary)

print("Total Salary:", total_salary)

print("IT Employee Names:", it_names)

print("Salary Dictionary:", salary_dict)

print("Grouped By Department:", grouped_by_dept)

print("Pipeline Result:", pipeline_result)

 
