def fibo():
    a, b = 1 , 0
    while a < n :
        print(a, end=' ')
        a, b = a + b , a

n = int(input('n='))
fibo(n)