wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}

def rsp(mine, yours):
    if mine == yours:
        return '비겼다'
    elif wintable[mine] == yours:
        return '내가 이겼다'
    else:
        return '내가 졌다'

print(rsp('가위','가위'))

list = [1,2,3,4,5]

list[2] = 33