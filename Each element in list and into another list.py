To check each element in the list and add into new list


n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(input())
    
for x in a:
    if 'a' in x:
        b.append(x)
print(b)
