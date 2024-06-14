'''A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.'''


#adding two numbers
'''def add(num1,num2):
    num3=num1+num2
    return num3
num1,num2=10,15
print(add(num1,num2))
'''
#method 1
'''def is_prime(n):
    for i in range(2,n):
        if n%i==0:
           return False
        else:
            return False
    return True
n=int(input("enter the number:"))
if is_prime(n):
    print("it is prime")
else:
    print("it is not prime")'''

#method 2
def check_prime():
    num=int(input("enter a number:"))
    if num>1:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                print("it is not prime")
                break
        else:
            print("it is prime")
    else:
        print("it is not prime")

check_prime()


 