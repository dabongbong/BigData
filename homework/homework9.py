def search (x,y,z):
    if x+y+z!= 180 or x==0 or y==0 or z==0:
        print('삼각형이 아닙니다')
    else:
        if max(x,y,z)>90 :
            print('둔각삼각형입니다')
        elif max(x,y,z)==90:
            print('직각삼각형입니다')
        else:
            print('예각삼각형입니다')
    return ''
x=int(input('제1각을 입력하세요'))
y=int(input('제2각을 입력하세요'))
z=int(input('제3각을 입력하세요'))
print(search(x,y,z))