s1=input()
n=len(s1)
s1=list(map(int,s1.split("/")))
if n!=10:
	print("no")
else:
	print("yes" if ((s1[0]<=31) and (s1[1]<=12)) else "no")
