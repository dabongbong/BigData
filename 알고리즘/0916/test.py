array = [5, 4, 7, 6, 8, 3, 1, 2, 9 ]
# arr = []
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# print(quick_sort(array))

def Quick_sort(a):
  pivot = a[-1]  
  a_left = []
  a_right = []

  for i in a:
    if i < pivot:
      a_left.append(i)
    else:
      a_right.append(i)
  return Quick_sort(a_left) + [pivot] + Quick_sort(a_right)


a = [5, 4, 7, 6, 8, 3, 1, 2, 9]
print(Quick_sort(array))

