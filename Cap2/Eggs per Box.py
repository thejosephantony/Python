# Typically 6 eggs fit in one box. Write a script to calculate the number of boxes a farmer needs to store 28 eggs. The script will also determine how many eggs are placed in the last uncompleted box, and how many additional eggs are needed to fill this last box.

num_ovos = 28
ovos_por_caixa = 6

num_de_caixas = num_ovos // ovos_por_caixa
caixa_incompleta = num_ovos % ovos_por_caixa


if(caixa_incompleta > 0):
    num_de_caixas = num_de_caixas + 1
else:
    num_de_caixas = num_de_caixas
    
ovos_restante = ovos_por_caixa - caixa_incompleta if caixa_incompleta > 0 else 0

print(f"Numero de caixas necessarias: {num_de_caixas}")
print(f"Ovos restantes para completar a ultima caixa: {ovos_restante}")
print(f"Ovos na ultima caixa: {caixa_incompleta if caixa_incompleta > 0 else ovos_por_caixa}")