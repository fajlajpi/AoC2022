with open("data/input_01_a.txt") as f:
    calories_data_raw = f.readlines()

calories_data = [line.strip() for line in calories_data_raw]

calories_sums = list()
current_tally = 0
for entry in calories_data:
    if entry != '':
        current_tally += int(entry)
    else:
        calories_sums.append(current_tally)
        current_tally = 0
calories_sums.sort(reverse=True)

print(f"Max value: {calories_sums[0]}")
print(f"Top three: {calories_sums[0] + calories_sums[1] + calories_sums[2]}")