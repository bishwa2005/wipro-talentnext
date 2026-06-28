data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

new_list = []

for item in data:
    new_tuple = item[:-1] + (100,)
    new_list.append(new_tuple)

print(new_list)