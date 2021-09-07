# 문자열이 불변의 성질을 가지고 있다면, 어떻게 새로운 문자열을 적립하거나 수정할 수 있을까?

a = 'Big '
a = a + 'Bad '
a = a + 'Dabong'
print(a)

n = ord('A')
s = ''
for i in range(n, n+26):
    s += chr(i)
print(s)

print('============================')

n = ord('A')
s = []
for i in range(n, n+26):
    s += chr(i)
print(s)

l = ', '.join(s)
print(l)