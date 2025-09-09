a = int(input())
b = int(input())
c = int(input())
d = int(input())

if ((a>b) and (a>d) and (a<c)) or ((a>c) and (a>d) and (a<b)) or (a>b) and (a>c) and (a<d):
	print(a)
elif ((b>a) and (b>d) and (b<c)) or ((b>a) and (b>c) and (b<d)) or ((b>c) and (b>d) and (b<a)):
	print(b)
elif ((c>a) and (c>d) and (c<b)) or ((c>b) and (c>a) and (c<d)) or ((c>b) and (c>d) and (c<a)):
	print(c)
else:
	print(d)