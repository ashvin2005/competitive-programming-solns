t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=[]
    for i in range(1,n):
        if s[i]!=s[i-1] :
            l.append(s[i-1])
        if s[i] in l :
            print("NO")
            break
    else:
        print("YES")
