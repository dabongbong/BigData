# dog1 = 'jaxx'
# dog2 = 'dabong'

# print(dog1, 'has', len(dog1), 'letters')
# print(dog2, 'has', len(dog2), 'letters')

# # is... 함수가 is로 시작하는 모든 메서드는 boolean값을 반환한다.

# str = '%%551gf'
# print(str.isalnum())    #isalnum => 글자와 숫자로만 이루어져 있는지 검사함. 최소한 한 글자 이상은 있어야함.
# print(str.isalpha())    #isalpha => 알파벳으로만 이루어져 있는지 검사. 최소 한글자 이상.
# print(str.isdecimal())  #isdecimal => 10진수 숫자로만 이루어져 있는지 검사.
# print(str.islower())    #islower => 소문자로만 이루어져 있는지 검사.
# print(str.isupper())    #isupper => 대문자로만 이루어져 있는지 검사.
# print(str.isspace())    #isspace => 공백으로만 이루어져 있는지 검사.
# print(str.istitle())    #istitle => 첫 글자만 대문자로 이루어져 있는지 검사.

#input 입력을 받아서 소문자인지, 대문자인지, 첫글자만 대문자인지, 숫자로만 이루어져 있는지 출력
# def chk():
#     str = input('문자를 입력해 주세요 : ')
#     if str.islower():
#         print('소문자로만 이루어져 있습니다.')
#     elif str.isupper():
#         print('대문자로만 이루어져 있습니다.')
#     elif str.istitle():
#         print('첫 글자만 대문자 입니다.')
#     elif str.isalnum():
#         print('숫자로만 이루어져 있습니다.')
#     else:
#         print('잘못 입력하셨습니다.')

# chk()

#대소문자로 변환하여 새로운 문자열을 만들자.
# str = "i'm Dabong"
# newstr = str.upper()
# newstr2 = str.lower()
# newstr3 = str.title()
# newstr4 = str.swapcase()
# print(newstr)
# print(newstr2)
# print(newstr3)
# print(newstr4)

# 접두어, 접미어 매서드
str = 'MR.Dabong Lee. PhD'
is_doc = str.endswith('PhD')
is_man = str.startswith('MR')
print(is_doc)
print(is_man)