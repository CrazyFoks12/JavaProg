# -- coding: utf-8 --
def sequence():
	s=str(input('Введите строку '))
	print (s[2])
	print (s[-2])
	print (s[0:5])
	print(s[:-2])
	print(s[::2])
	print(s[1::2])
	print(s[::-1])
	print(s[::-2])
	print(len(s))
print(sequence())