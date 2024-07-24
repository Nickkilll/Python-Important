To count the occurence of a character:


n=int(input())
a=list(map(str,input().split()))
for i in a:
    b=i.count('a')
    print(b,end=" ")
    
