print("HOLA MUNDO!!!! ")
print(" PYTHON?")
name = input("Your name: ")
print("Hello,",name,"- nice to meet you!")
a = float(input("INGRESE EL 1ER NUMERO: "))
b = float(input("INGRESE EL 1ER NUMERO: "))
print("SUMA:", a + b)
print("RESTA", a - b)
print("MULTIPLICACION:", a * b)
print("DIVISION:", a / b)
n = int(input("INGRESE UN NUMERO: "))
print(n >= 100)

year = int(input("Enter a year: "))
if year < 1582:
	print("Not within Gregorian calendar's period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")
