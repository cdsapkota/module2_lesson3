temp_above_100 = []
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

for count in temperatures:
    if count > 100:
        temp_above_100.append(count)
    else:
        pass

print(temp_above_100)
