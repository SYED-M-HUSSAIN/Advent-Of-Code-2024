meta_data = []
filepath = "/workspaces/Advent-Of-Code-2024/DAY2/input.txt"
with open(filepath, "r") as file:
    for line in file:
        values = line.strip().split()
        data = []
        for x in values:
            data.append(int(x))
        meta_data.append(data)



        


