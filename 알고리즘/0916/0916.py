arrayD = [12, 25, 36, 20, 30, 8, 42]
arrayH = [0 for i in range(11)]
i = 0

for i in range (0, len(arrayD)) : 
    k = arrayD[i] % 11
    while True :
        if arrayH[k] == 0:
            arrayH[k] = arrayD[i]
            break
        else :
            k = (k + 1) % 11
print(arrayH)

x = int(input('찾는 값 : '))

k = x % 11

while True:
    if arrayH[k] != 0:
        if arrayH[k] == x:
            print("저장 위치는 {}입니다.".format(k))
            break
        else :
            k = (k+1) % 11
    else :
        print("존재하지 않는 값입니다")
        break