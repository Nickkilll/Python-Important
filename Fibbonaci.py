Fibbonaci Number


a=int(input())
n1=0
n2=1
print(n1,n2,end=' ')
for i in range(a+1):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=' ')
