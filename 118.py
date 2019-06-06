l=[str(x) for x in input().split()]
l1=""
for i in l:
	if len(i)>len(l1):
		l1=i
for i in l:
	if l1==i:
		print(i)
		break
