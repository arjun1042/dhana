"""
n = int(input())
arr = list(map(int,input().split()))
lis = [1]
count = 0
for i in range(1,n):
    if arr[i]> arr[i-1]:
        lis.append(lis [count] + 1)
        count = count+1
    elif arr[i-1] == arr[i]:
        lis.append(lis[count])
        count=count+1
print(sum(lis))

n = int(input())
arr = list(map(int,input().split()))
lis = [1]
count = 0
for i in range(1,n):
if arr[i]> arr[i-1]:
lis.append(lis [count] + 1) count = count+1
elif arr[i-1] == arr[i]: lis.append(lis[count]) count count+1 print(sum(lis))

import math
from collections import Counter
string=input()
count_=Counter(string)
Nresult=math.factorial(len(string))
Dresult=1
for i in count_.value():
    Dresult*=math.factorial(i)
print((Nresult//Dresult))

from collections import deque

n = int(input())
a = []
for i in range(n):
    a.append(input())
    
used = [[False for i in range(n)] for i in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if used[i][j] or a[i][j] == 'W':
            continue
        q= deque()
        q.append((i, j))
        used[i][j] = True
        cnt = 0
        while q:
            (x, y) = q.pop()
            cnt += 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                X_= x + dx
                y_= y + dy
                if x_ >= 0 and x < n and y_ >= 0 and y_ < n:
                    if not used[x][y] and a[x][y_] == 'T':
                        q.append((x_, y_))
                        used [x_][y_] = True
        ans = max(ans, cnt)
print(ans)"""

