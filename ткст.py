from random import randint
n = int(input())
num = [[randint(1,10) for i in range(n)] for j in range(n)]
for i in num :
    print(*map('{:2d}'.format, i))
print()
for i in range(n//2 + n%2) :
    for j in range(n-i) :
        num[i][j] = 1
for i in num :
    print(*map('{:2d}'.format, i))