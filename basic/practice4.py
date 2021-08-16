gender = "남자"
height = 175

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    elif gender == "여자":
        return height * height * 21

    return weight
# gender = input("성별을 입력 하세요")
# height = int(input("키를 입력하세요"))

weight = std_weight(height / 100, gender)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다".format(height, gender, round(weight,2)))