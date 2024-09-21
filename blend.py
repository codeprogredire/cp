#link: https://codeforces.com/contest/2013/problem/A

import math
t=int(input())

while t>0:
    n=int(input())
    x,y=map(int,input().split())
    print(int(math.ceil(n/min(x,y))))

    t-=1

