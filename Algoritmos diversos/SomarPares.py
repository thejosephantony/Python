# Some todos os números pares entre 1 e 100 usando for.
soma = 0
for i in range(1,101):
    if(i % 2 == 0):
        soma = i + soma
print(f"A soma dos números pares entre 1-100 é de {soma}\n")