# month = ['jan','feb','mar','apr','may','jun']

# for i in enumerate(month):
#     print(i)

# for i, name in enumerate(month):
#     print('{}월은 {}입니다'.format(i+1,name))
import urllib.request

classroom = {'1반':[162,175,198,137,145,199], '2반':[165,177,157,160,191]}

try:
    for i,j in classroom.items():
        for k in j:
            if k > 190:
                print("{}에 190이 넘는 학생이 있습니다.".format(i))
                raise StopIteration
except StopIteration:
    print("190이 넘는 학생을 찾았습니다.")