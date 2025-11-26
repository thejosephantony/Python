# Conte quantos números positivos foram digitados entre 10 valores inseridos.

contador = 0

for i in range(1,11):
    num = int(input(f"Insira o numéro {i}: \n"))
    if(num >= 0):
        contador = contador + 1

print(f"Foram digitados {contador} números positivos.\n")