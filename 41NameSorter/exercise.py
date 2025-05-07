with open("names.txt") as f:
    names = [line.strip() for line in f if line.strip()]

names.sort()

with open("sorted_names.txt", "w") as f:
    f.write(f"Total of {len(names)} names\n")
    f.write("-----------------\n")
    for name in names:
        f.write(name + "\n")
