# Peça ao usuário 5 números e mostre o menor deles.

num1 = int(input("Número 1: \n"))
num2 = int(input("Número 2: \n"))
num3 = int(input("Número 3: \n"))
num4 = int(input("Número 4: \n"))
num5 = int(input("Número 5: \n"))

menor = None
maior = None

for numero in [num1, num2, num3, num4, num5]:
    if(menor is None or numero < menor):
        menor = numero
    if (maior is None or numero > maior):
        maior = numero

print(f"O menor número é o {menor}\n")
print(f"O maior número é o {maior}\n")