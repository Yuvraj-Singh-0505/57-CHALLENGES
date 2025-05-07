employees = [
    {"first_name": "John", "last_name": "Johnson", "position": "Manager", "separation_date": "2016-12-31"},
    {"first_name": "Tou", "last_name": "Xiong", "position": "Software Engineer", "separation_date": "2016-10-05"},
    {"first_name": "Michaela", "last_name": "Michaelson", "position": "District Manager", "separation_date": "2015-12-19"},
    {"first_name": "Jake", "last_name": "Jacobson", "position": "Programmer", "separation_date": ""},
    {"first_name": "Jacquelyn", "last_name": "Jackson", "position": "DBA", "separation_date": ""},
    {"first_name": "Sally", "last_name": "Weber", "position": "Web Developer", "separation_date": "2015-12-18"}
]

search = input("Enter a search string: ").lower()

print("Results:")
print("Name                 | Position             | Separation Date")
print("---------------------|----------------------|------------------")

for e in employees:
    if search in e["first_name"].lower() or search in e["last_name"].lower():
        name = e["first_name"] + " " + e["last_name"]
        position = e["position"]
        date = e["separation_date"]
        print(f"{name:<21}| {position:<21}| {date}")
