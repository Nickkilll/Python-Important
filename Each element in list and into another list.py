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


// Another method of using comprehension

n=int(input())
a=[]

for i in range(n):
    a.append(input())
b=[x for x in a if 'a' in x]
print(b)
