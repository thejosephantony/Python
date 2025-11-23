a = float(input("Digite o primeiro tempo (segundos): "))
b = float(input("Digite o segundo tempo (segundos): "))
c = float(input("Digite o terceiro tempo (segundos): "))

print("\nValores em ordem crescente:")

# Verifica a ordem usando comparações
if a <= b and a <= c:
    menor = a
    if b <= c:
        meio = b
        maior = c
    else:
        meio = c
        maior = b

elif b <= a and b <= c:
    menor = b
    if a <= c:
        meio = a
        maior = c
    else:
        meio = c
        maior = a

else:  # c é o menor
    menor = c
    if a <= b:
        meio = a
        maior = b
    else:
        meio = b
        maior = a

print(menor, meio, maior)