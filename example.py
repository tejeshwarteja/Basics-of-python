#watermelon problem
w=2
if (w%2 !=0 or w==2):
    print("no")
else:
    x=w/2
    if(x%2==0):
        print("weight of 2 pieces are:",x,x)
    else:
        print("weight of 2 pieces are",x-1,x+1)
