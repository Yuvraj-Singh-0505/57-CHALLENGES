with open("data.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

records = []
for line in lines:
    parts = line.split(",")
    records.append(parts)

max_last = max(len(r[0]) for r in records) + 1
max_first = max(len(r[1]) for r in records) + 1
max_salary = max(len(r[2]) for r in records)

print("Last".ljust(max_last), end="")
print("First".ljust(max_first), end="")
print("Salary")

print("-" * (max_last + max_first + max_salary))

for r in records:
    print(r[0].ljust(max_last), end="")
    print(r[1].ljust(max_first), end="")
    print(r[2])
