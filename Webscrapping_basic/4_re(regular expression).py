import re       # regular expression (정규식)

p = re.compile("ca.e")
# . : 하나의 문자(ca.e) -> cave, cafe, case(o) / caffe(x)
# ^ : 문자열의 시작(^de) -> de 로 시작하는 문자열
# $ : 문자열의 끝(se$) -> case, base(o) / face(x)

#print(m.group())    #매칭이 안돼면 에러

def print_match(m):     #예외처리 함수
    if m:
        print("m.group() :", m.group())    # 일치하는 문자열 반환
        print("m.string() :", m.string)    # 입력받은 문자열 // 변수
        print("m.start() :", m.start())    # 일치하는 문자열의 시작 index
        print("m.end() :", m.end())        # 일치하는 문자열의 끝 index
        print("m.span() :", m.span())      # 일치하는 문자열의 시작, 끝 index
    else :
        print("매칭되지 않음")

# m = p.match("lesscase")     # 주어진 문자열이 처음부터 일치하는지 확인
# print_match(m)

m = p.match("caseless")
print_match(m)

# m = p.search("good care")     # 주어진 문자열 중 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("caseless care cafe caffe")       # 일치하는 모든 것을 "리스트" 형태로 반환
print(lst)

## 정리
# 1. p = re.compile("원하는 정규식 형태")
# 2. m = p.match("비교할 문자열 ")
# 3. m = p.search("비교할 문자열")
# 4. lst = p.findall("비교할 문자열")

## 정규식
# . : 하나의 문자(ca.e) -> cave, cafe, case(o) / caffe(x)
# ^ : 문자열의 시작(^de) -> de 로 시작하는 문자열
# $ : 문자열의 끝(se$) -> case, base(o) / face(x)

## 참고사이트 : w3school, docs.python.org(google : python re)