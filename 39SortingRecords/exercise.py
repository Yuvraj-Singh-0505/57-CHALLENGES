employees = [
    {"first_name": "John", "last_name": "Johnson", "position": "Manager", "separation_date": "2016-12-31"},
    {"first_name": "Tou", "last_name": "Xiong", "position": "Software Engineer", "separation_date": "2016-10-05"},
    {"first_name": "Michaela", "last_name": "Michaelson", "position": "District Manager", "separation_date": "2015-12-19"},
    {"first_name": "Jake", "last_name": "Jacobson", "position": "Programmer", "separation_date": ""},
    {"first_name": "Jacquelyn", "last_name": "Jackson", "position": "DBA", "separation_date": ""},
    {"first_name": "Sally", "last_name": "Weber", "position": "Web Developer", "separation_date": "2015-12-18"}
]

sorted_employees = sorted(employees, key=lambda e: e["last_name"])

print("Name                 | Position             | Separation Date")
print("---------------------|----------------------|------------------")

for e in sorted_employees:
    name = e["first_name"] + " " + e["last_name"]
    position = e["position"]
    date = e["separation_date"]
    print(f"{name:<21}| {position:<21}| {date}")
