# list = [1,2,3,4,5]
# for i, v in enumerate(list):
#     print('{}번 값 : {}'.format(i,v))

# select = None
# while select not in ['가위', '바위', '보']:
#     select = input('가위, 바위, 보 중에서 선택하세요>')
# print('선택한 값은 : ', select)

pattern = ['가위', '바위', '보']
for i in range(len(pattern)):
    print(pattern[i])
i = 0
while i < len(pattern):
    print(pattern[i])
    i += 1 