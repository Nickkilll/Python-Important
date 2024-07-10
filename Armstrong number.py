ARMSTRONG NUMBER:

code:
f=int(input())
b=str(f)
length=len(b)
sum=0
for i in range(length):
    d=int(b[i])
    sum=sum+pow(d,length)
if(f==sum):
    print("ARM")
else:
    print("NO ARM")
