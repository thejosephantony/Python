# Escreva um programa que leia um número inteiro positivo e determine se ele é primo usando um loop simples (testando todos os números de 1 até ele).

divisores = 0
num = int(input("Digite um número: \n"))

if(num <= 1):
    print("Não é primo")
else:
    primo = True
    for i in range(2, num):
        if(num % i == 0):
            primo = False
            break
        
    if primo:
        print(f"{num} é primo")
    else:
        print(f"{num} não é primo")