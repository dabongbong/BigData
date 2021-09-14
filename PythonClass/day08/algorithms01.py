arr = [12,13,11,14,10]
max = arr[0]
i = 1

while i < 5:
    if arr[i] > max:
        max = arr[i]
    i = i + 1
print(max)
