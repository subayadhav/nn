s1,k=map(str,input().split())
if len(s1)>len(k):
    p=s1
    r=k
    print(p[0:len(r)]+r)
else:
    p=k
    r=s1
    print(r[0:len(p)]+p)
