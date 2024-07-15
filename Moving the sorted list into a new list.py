Moving the sorted list into a new list


n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(input())
b=sorted(a)
for i in b:
    print(i,end=" ")
