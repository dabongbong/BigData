head = 0
tail = 6
array = [11, 13, 17, 19, 23, 29, 31]

while True:
    mid = (head+tail)/2
    if array[mid] < 17:
        head = mid + 1
    elif array[mid] > 17:
        tail = mid - 1
    else:
        print("{}번째 요소가 동일".format(mid))
        break
    if head <= tail:
        print("찾지 못했습니다.")
        break
