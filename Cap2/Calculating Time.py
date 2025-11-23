# converter segundos para um relógio hora-minutos-segundos

segundos = int(input("Segundos: "))

hrs = segundos // 3600
min = (segundos % 3600) // 60
seg = segundos % 60

print(f"{hrs} - {min} - {seg} ")
