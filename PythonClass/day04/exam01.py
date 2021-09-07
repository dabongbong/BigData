# 문자열은 불변이다.
# mutable 가변, dic, set, list              immutable 불변  tuple

result 
n = int(input('자리수를 알고싶은 숫자를 입력하세요'))
if len(str(num)) == 1:
    result = '한자리 수'
elif len(str(num)) == 2:
    result = '두자리 수'
else:
    result = '세자리 수'


print(n,'의 자릿수는',   ,'입니다.')