LCM OF N NUMBERS:


a=int(input())
b=int(input())
c=int(input())
i=1
while(1):
    if(i%a==0 and i%b==0 and i%c==0):
        print(i)
        break
    else:
        i=i+1
