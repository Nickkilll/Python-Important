Extend Function:
to join 2 lists in Python:

a=[]
b=[]
n=int(input())
for i in range(n):
    a.append(int(input())) // elements of a list
    b.append(int(input())) //elements of b list
    
a.extend(b) //joined a and b in single list
for i in a:
    print(i,end=" ")
