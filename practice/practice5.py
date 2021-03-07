
# score_file = open("score.txt","w",encoding ="utf8")
# print("DATA 1 : 10",file=score_file)
# print("DATA 2 : 30",file=score_file)
# print("DATA 3 : 50",file=score_file)
# print("DATA 4 : 100",file=score_file)

# score_file.close() 


score_file = open("score.txt","r",encoding ="utf8")

lines = score_file.readlines()
for line in lines:
    print(line,end="")

score_file.close()  