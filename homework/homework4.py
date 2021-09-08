#211
def string(st):
    print(st)

string("안녕")
string("HI")

print("==========")
#212
def defi(a,b):
    print(a+b)

defi(3,4)
defi(7,5)
print("==========")
#213
def a(s1):
    print(s1)
a("매개변수") #매개변수를 넘겨주지 않아 오류가 뜸
print("==========")

#214
def a214(a,b):
    print(a+b)
a214('안녕', "3") #매개변수로 형태가 다름, string형과 int형은 연산이 불가능함
print("==========")
#215
def print_with_smile(s215):
    print(s215, end=":D\n")

print("==========")
#216
print_with_smile("안녕하세요")

print("==========")
#217
def print_upper_price(i217):
    print(int(i217)*1.3)
print_upper_price(30000)
print("==========")

#218
def print_sum(a,b):
    print(a+b)

print_sum(3,4)
print("==========")

#219
def print_arithmetic_operation(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
print_arithmetic_operation(3,4)
print("==========")

#220
def print_max(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)
    else:
        print("서로 다른 수를 입력해 주세요.")
print_max(3,6,9)
print("==========")

#221
def print_reverse(s221):
    reverse = ""
    for i in s221:
        reverse = i + reverse
    print(reverse)
        
print_reverse("python")
print("==========")

#222
def print_score(score):
    sum = 0
    for i in score:
        sum += i
        print(sum)
    print(sum/len(score))
print_score([10,2,3])
print("==========")
#223
def print_even(l223):
    li = []
    for i in l223:
        if i % 2 == 0:
            li.append(i)
    print(li)

print_even([1,3,2,10,12,11,15])
print("==========")

#224
def print_keys(dic224):
    print(dic224.keys())

print_keys({"이름":"김말똥", "나이":30, "성별":0})
