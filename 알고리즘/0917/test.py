arr =[1] * 100
k = 2
# print(arr)
while k * k <= 100: 
    if arr[k] == 1:
        i = k
        while i <= 99/k:
            arr[k*i] = 0 
            # print(k*i)
            i = i + 1
    k = k + 1
    break
    
i = 2
while True:
    if i <= 99:
        if arr[i] == 1:
            print(i, end=(', '))
        i = i + 1
    else : 
        break