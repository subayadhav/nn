n=int(input())
l=[int(i) for i in input().split()]
s=[]
a=0
for i in range(n):
	a+=l[i]
	s.append(a)
print(*s)
