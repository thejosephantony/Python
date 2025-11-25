# Binary-to-Decimal Conversion

num_binario = int(input("Insira o número em binário: \n"))
num_original = num_binario
num_decimal = 0
potencia = 1

while num_binario > 0:
    ultimo_digito = num_binario % 10
    num_decimal = num_decimal + ultimo_digito*potencia
    potencia = potencia*2
    num_binario= num_binario // 10
    
print(f"O equivalente decimal do binário {num_original} é {num_decimal}\n")
    
    