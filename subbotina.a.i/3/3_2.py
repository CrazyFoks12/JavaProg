# -- coding: utf-8 --
def sequence():
	a=int(input('a='))
	b=int(input('b='))
	if a<b:
		for i in range(a, b+1):
			print(i)
	else:
		for i in range(a,b-1,-1):
			print(i)
print(sequence())