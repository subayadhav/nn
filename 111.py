n1,k=map(int,input().split())
l=[int(i) for i in input().split()]
t=l[0:n1]
s=l[n1:]
l=[]
for i in t:
	if i in s:
		l.append(i)
		s.remove(i)
print(*(l))
