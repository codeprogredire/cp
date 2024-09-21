#link: https://codeforces.com/contest/2014/problem/0

t=int(input())

while t>0:
    n,k=map(int,input().split())
    store=list(map(int,input().split()))

    bank,count=0,0
    for i in range(n):
        if store[i]>=k:
            bank+=store[i]
        elif store[i]==0 and bank>0:
            store[i]+=1
            bank-=1
            count+=1

    print(count)
    t-=1