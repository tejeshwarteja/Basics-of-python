def check_number(n):
        
    if n%2==1:
        print("Weird")
        if n%2==0:
            for n in range(2,6):
                print("Not Weird")
        else:
            for n in range(6,21):
                break
                print("Weird")
                
    else:
        print("Not Weird")
            
num = int(input(""))
check_number(num)
