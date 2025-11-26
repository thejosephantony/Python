# Leia um número e diga se é positivo, negativo ou zero.

num = int(input("Número: \n"))

if(num == 0):
    print(f"O número {num} é zero.\n")
elif(num < 0):
    print(f"O número {num} é negativo.\n")
else:
    print(f"O número {num} é positivo.\n")