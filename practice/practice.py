from random import *
#id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
id = range(1,21)
id = list(id)


chicken = id.pop(int(random() * len(id)))
print(id)
# coffee = id[int(random() * 19 + 1),int(random() * 19 + 1),int(random() * 19 + 1)]
coffee = [id.pop(int(random() * len(id))), id.pop(int(random() * len(id))), id.pop(int(random() * len(id)))]
print(id)
coffee.sort()
print("-- 당첨자 발표 --")
print("치킨 당첨자 : " + str(chicken))
print("커피 당첨자 : " + str(coffee[0]), str(coffee[1]), str(coffee[2]))
print("-- 축하 합니다. --")

print(id, type(id))

