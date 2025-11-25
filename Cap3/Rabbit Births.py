coelhas = 0
babyCoelhos = 0
totalCoelhas = 0
totalBabyCoelhos = 0


while(True):
    coelhas = int(input("Qual o número de coelhas na colônia? (-1 para sair)\n"))
    if(coelhas == -1):
        break
    babyCoelhos = int(input("Qual o número de baby coelhos nascidos?\n"))
    totalCoelhas+=coelhas
    totalBabyCoelhos+=babyCoelhos
    
media = totalBabyCoelhos/totalCoelhas
print(f"A média é de {media}")
    
    