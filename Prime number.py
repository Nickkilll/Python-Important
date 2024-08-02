Prime number:


def prime(n):
     if n<=2:
        return 0
     for i in range(2,n):
        if n%i==0:
            return 1
            
n=int(input())
flag=prime(n)
if(flag):
    print("No prime")
else:
    print("Prime")
