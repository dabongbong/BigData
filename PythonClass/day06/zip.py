#   zip()
students = ['임진영', '강은미', '정준식', '임다혜', '김영진', '김성현']
scores = [90, 98, 97, 100, 96, 92, 93]

for x, y in zip(students, scores):
    print(x,y)
for x in zip(students, scores):
    print(x)
# zip 함수는 리스트 두개 이상을 받아서 모든 리스트의 0번 인덱스 값이 든 튜플, 모든 리스트의 1번 인덱스 값이 든 튜플.....
# 을 순서대로 만드는 함수이다.

# zip을 이용한 딕셔너리 조건제시법.

students = ['임진영', '강은미', '정준식', '임다혜', '김영진', '김성현']
scores = [90, 98, 97, 100, 96, 92, 93]

score_dic = {student:score for student, score in zip(students,scores)}
print(score_dic)