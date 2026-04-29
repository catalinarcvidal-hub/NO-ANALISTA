t=5247321
x=0
z=0
c=0
while t > 0:
	c = t % 10
	if c % 2 == 1:
		x = x + 1
	else:
		z = z + 1
	t = t // 10
print(x)
print(z)

"""
Evaluar con traza que realiza el if y else con el numero de T.

"""