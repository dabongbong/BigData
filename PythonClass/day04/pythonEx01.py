# 전역 변수와 지역 변수

count = 10      # 전역변수의 선언

def funcA():
    count = 20  #지역변수 선언
    print(count)#지역변수 출력

def funcB():
    print(count)#전역변수 10 출력

funcA()
funcB()