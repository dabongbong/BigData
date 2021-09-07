def main():
    side1 = float(input('한 변의 길이를 입력하세요 : '))
    side2 = float(input('다른 한 변의 길이를 입력하세요 : '))

    hyp = ((side1 * side1) + (side2 * side2)) ** 0.5

    print('빗변의 길이는', hyp, end=' ')
    print('입니다')


main()