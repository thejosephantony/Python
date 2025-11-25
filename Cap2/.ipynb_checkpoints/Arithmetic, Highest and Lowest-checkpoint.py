# Arithmetic, Highest and Lowest

nota_matemática = int(input("Informe a nota de Matemática (em inteiro): "))
nota_português = int(input("Informe a nota de Português (em inteiro): "))
nota_ciências = int(input("Infore a nota de Ciências (em inteiro): "))

# Média das Notas
media_notas = (nota_matemática + nota_ciências + nota_português)/3
print(f"A média das notas foi de {media_notas:.2f}\n")

#Maior Nota
if(nota_matemática > nota_português and nota_matemática > nota_ciências):
    print(f"A disciplina com a maior nota foi de Matemática com {nota_matemática}\n")
elif(nota_português > nota_matemática and nota_português > nota_ciências):
    print(f"A disciplina com a maior nota foi de Português com {nota_português}\n")
elif(nota_ciências > nota_matemática and nota_ciências > nota_português):
    print(f"A disciplina com a maior nota foi de Ciências com {nota_ciências}\n")
else:
    print("As notas foram iguais\n")
    
# Menor nota
if(nota_matemática < nota_português and nota_matemática < nota_ciências):
    print(f"A disciplina com a menor nota foi de Matemática com {nota_matemática}\n")
elif(nota_português < nota_matemática and nota_português < nota_ciências):
    print(f"A disciplina com a menor nota foi de Português com {nota_português}\n")
else:
    print(f"A disciplina com a menor nota foi de Ciências com {nota_ciências}\n")

