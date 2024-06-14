#first and last element swapping and sorting list
a=input().split()
a.sort(key=len)
first=a[0]
last=a[-1]
a[0],a[-1]=last, first
print(a)

n=int(input())
a = [map(int,input().split()) for i in range(n)]
m=0
for i in a:
    s= sum(1)
    if