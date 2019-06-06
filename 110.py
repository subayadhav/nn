ns=int(input())
l=[int(i) for i in input().split()]
s=[]
a=0
for i in range(ns):
	a+=l[i]
	s.append(a)
t=s[::-1]
l=[]
for j in range(ns):
	k=t[j]+s[j]
	l.append(k)
print(*l)
