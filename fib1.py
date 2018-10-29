def fib (n):
	if n < 2:
		return n
	return fib(n-3)+fib(n-1)


n = int(input("Enter the number of times you want to input n :"))
for i in range (n):
	a = int(input ("Enter number :"))
	print fib(a)
