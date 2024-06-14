n=[5,4,3,2,1]
m=[1,2,3,4,5]
k=[]
l=[]
for i in range(len(n)):
    if n[i]%2==0:
        k.append(n[i]+2)
    else:
        k.append(n[i]+1)
for j in range(len(m)):
    if m[j]%2==0:
        l.append(m[j]+2)
    else:
        l.append(m[j]+1)
print(k)
print(l)

