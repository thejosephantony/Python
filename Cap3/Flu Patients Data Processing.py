# Flu Patients Data Processing) During the flu season, it is important to keep track
#  of the number of infected patients. Write a script in which the user can input the number
#  of reported infections per day over one week. Calculate the total, average, smallest, and
#  largest of these values. Write your script using a loop structure.

total = 0
maior = None
menor = None


for dia in range(1,8):
    infecções = int(input(f"Informe o número de infecções no dia {dia}: \n"))
    total += infecções
    
    if(menor is None or menor > infecções):
        menor = infecções
    if(maior is None or maior < infecções):
        maior = infecções
    
media = total/7

print(f"O total de infecções foi de {total}\n")
print(f"A média de infecções foi de {media}\n")
print(f"O maior número de infecções foi de {maior}\n")
print(f"O menor número de infecções foi de {menor}\n")
    
    
    