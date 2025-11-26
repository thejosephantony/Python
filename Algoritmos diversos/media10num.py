# Leia 10 números e imprima a média deles.
soma = 0
for i in range(1,11):
    num = int(input(f"Insira o numéro {i}: \n"))
    soma = num + soma
    
media = soma/10
print(f"A média é de {media:.2f}\n")