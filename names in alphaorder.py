#code to take names and then sort them in alphabetical
from collections import Counter

names = []
name_count = 0

print("Enter a list of names, one per line. Type 'submit' when finished.")

while True:
    name = input()
    if name.lower() == "submit":
        break
    names.append(name)
    name_count += 1

# Count the occurrences of each name and sort names alphabetically
name_counts = Counter(names).most_common()

# Print the results
print(f"\nTotal names entered: {name_count}")
print("\nFinal sorted list of names with counts:")

for name, count in name_counts:
    print(f"{name} ({count})")