n1=int(input())
l=list(map(int,input().split()))
a=list(set(l))
a.sort(reverse=True)
b=[]
d=[]
c=0
for i in a:
	b.append(l.count(i))
while c<len(b):
	s=b.index(max(b))
	d.append(a[s])
	b[s]=0
	c=c+1
print(*d)
