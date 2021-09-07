from random import randint

n = randint(1,50)

while True:
    ans = int(input('어떤 숫자일까요? : '))
    if ans > n:
        print('높습니다. 다시 시도하세요!')
    elif ans < n:
        print('낮습니다. 다시 시도하세요!')
    else:
        print('정답입니다!')
        break
