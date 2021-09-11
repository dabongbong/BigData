import datetime

now = datetime.datetime.now()

if now.hour > 12 :
    print("현재 시간은 {}시로 오후입니다".format(now.hour))
else:
    print("현재 시간은 {}시로 오전입니다".format(now.hour))

mon = now.month
if 3 <= mon <= 5:
    print("이번달은 {}월로 봄입니다".format(mon))
elif 6 <= mon <= 8:
    print("이번달은 {}월로 여름입니다".format(mon))
elif 9 <= mon <= 11:
    print("이번달은 {}월로 가을입니다".format(mon))
else :
    print("이번달은 {}월로 겨울입니다".format(mon))

num = int(input("숫자입력 : "))

zodiac = ["쥐","소","호랑이","토끼","용","뱀","말","양","원숭이","닭","개","돼지"]
birth = int(input("생년월일 : "))
if 