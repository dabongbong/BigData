inventory = {'메로나' : [300, 20], '비비빅' : [400, 3], '죠스바' : [250, 100]}
# print(inventory)
price = inventory['메로나'][0]
# print('%i원'%price)
stk = inventory['메로나'][1]
# print('%i개'%stk)
inventory['월드콘'] = [500, 7]
# print(inventory)

icecream = {"탱크보이" : 1200, "폴라포" : 1200, "빵빠레" : 1800, "월드콘" : 1500, '메로나' : 1000}
name = icecream.keys()
price2 = list(icecream.values())
# print(name)
# print(price2)
tPrice = 0
for i in range(0, len(price2)):
    tPrice += price2[i]
# print(tPrice)
new_product = {"팥빙수" : 2700, "아맛나" : 1000}
icecream.update(new_product)
# print(icecream)

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))
# print(result)

date = ["09/05", "09/06", "09/07", "09/09"]
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
# print(close_table)

# list = [3, -20, -3, 44]
# for i in list:
#     if i < 0:
        # print(i)

# num = [3, 100, 23, 44]
# for i in num:
#     if i % 3 == 0:
#         print(i)

# list = [13, 21, 12, 14, 30, 18]
# for i in list:
#     if i < 20 and i % 3 == 0:
#         print(i)

# list = ["I", "study", "python", "language", "!"]
# for i in list:
#     if len(i) > 3:
#         print(i)

# list = ["A", "b", "c", "D"]
# for i in list:
#     if i.isupper():
#         print(i)

# for i in list:
#     if i.islower():
#         print(i)

# list = ['dog', 'cat', 'parrot']

# for i in list:
#     a = i.title()
#     print(a)

# list = ["hello.py", "ex01.py", "intro.hwp"]
# for i in list:
#     a = i.split(".")
#     print(a[0])

list = ["intra.h", "intra.c", "define.h", "run.py"]
# for i in list:
#     if i[-2:] == ".h" :
#         print(i)

# for i in list:
#     if i[-2:] == ".h" or i[-2:] == ".c":
#         print(i)