#key and values are used in dict.
#its mutable
#duplicate keys are not allowed but values can be duplicated.
'''d={1:'kiran', 2:'harsha', 100:32.4, 'a':123}
for i in d:
    print(i,":",d[i])
#       print(d.get(1))
'''

#taking two dictionary input and joining them.
'''d={}
d1={}
n= int(input("no of elements"))
for i in range(n):
    k= input("enter key for dict:")
    v= input("enter its value:")
    d[k]=v
for i in range(n):
     k= input("enter key for dict:")
     v= input("enter its value:")
     d1[k]=v
d2=d.copy()
d2.update(d1)
print(d2)'''


#removing one key by input
'''d1={}
n= int(input("no of elements"))
for i in range(n):
    k= input("enter key for dict:")
    v= input("enter its value:")
    d1[k]=v
b=input("enter removing key")
if b in d1:
    d1.pop(b)
print(d1)'''


#taking two lists inputs and joining them as key and values respectively.
l1=input().split()
l2=input().split()
d=dict(zip(l1,l2))
print(d)