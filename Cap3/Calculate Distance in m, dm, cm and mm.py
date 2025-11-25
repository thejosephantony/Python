#  (Calculate Distance in m, dm, cm and mm) A trainer wants to calculate the addi
# tional distance an athlete needs to jump to break the world record for the longest long
#  jump (8.85 m). Write a script that accepts the current jumping distance of the athlete in
#  meters as input. Display the difference in distance between the world record and the cur
# rent jump in m, dm, cm, and mm. For example, when an athlete jumps 6.43 m, the script
#  would output:
#  You need to jump: 2.42 additional meters to improve the world record.
#  Meters: 2.0
#  Decimeters: 4.0
#  Centimeters: 2.0
#  Millimeters: 0.0

distanciaAtual = float(input("Informe a distância do salto atual: \n"))
recorde = 8.85
diferenca = recorde - distanciaAtual

metros = int(diferenca)
resto = diferenca - metros

decimetros = int(resto*10)
resto = resto*10 - decimetros

centimetros = int(resto*10)
resto = resto*10 - centimetros

milimetros = int(resto*10)

print(f"Você precisa saltar: {diferenca} adicionais para quebrar o recorde mundial\n")
print(f"Metros: {metros}")
print(f"Decimetros: {decimetros}")
print(f"Centimetros: {centimetros}")
print(f"Milimetros: {milimetros}")
