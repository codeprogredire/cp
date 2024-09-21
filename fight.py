# link: https://codeforces.com/contest/2013/problem/B

t=int(input())

while t>0:
    n=int(input())
    fighters=list(map(int,input().split()))

    penultimate=fighters[-2]

    for i in range(n-3,-1,-1):
        penultimate-=fighters[i]

    print(fighters[-1]-penultimate)

    t-=1