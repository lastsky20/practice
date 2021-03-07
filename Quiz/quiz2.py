table_list = []

for i in range(1,20):
    table_list.append("A" + str(i))

print(table_list)

for a in range(0, 19):
    tmp1 = int(table_list[a][1:])
    if tmp1 % 2 == 1:
        print(table_list[a], end=" ")
    