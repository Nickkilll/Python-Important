Count the list elements which has 2,3,4 ... digits

n= int(input())
a=list(map(int,input().split()))
b=0
for i in a:
    b += sum(int(j) for j in str(i))
