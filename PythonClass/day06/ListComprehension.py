# List Comprehension ( 리스트 내포, 조건제시법 )
# 원하는 구성 요소를 하나씩 집어 넣는 대신 코드를 이용해 리스트나
# 딕셔너리를 바로 생성하는 방법.

areas = []
for i in range(1,11):
    areas = areas + [i*i]
# print(areas)

# print([i * i for i in range (1,11)])

# print([i for i in range(1,101) if i % 8 == 0])

students = ['임진영', '강은미', '정준식', '임다혜', '김영진', '김성현']
for num, name in enumerate(students):
    print("{}번의 이름은 {}입니다.".format(num + 1, name))



student_dict = {"{}번".format(num+1) : name for num, name in enumerate(students)}

print(student_dict)