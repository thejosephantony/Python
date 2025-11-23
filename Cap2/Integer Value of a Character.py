# exibir o valor inteiro de um caractere

# Tom e Jim querem jogar um jogo, mas não conseguem decidir quem começa.
# Eles decidem que a pessoa com a soma mais alta dos valores inteiros dos caracteres do próprio nome será a que joga primeiro.
# Escreva um script para determinar quem começa.

Soma_Tom = ord('T') + ord('o') + ord('m')
Soma_Jim = ord('J') + ord('i') + ord('m')

if(Soma_Tom > Soma_Jim):
    print(f"Tom começa o jogo, pois a soma dos caracteres do seu nome deu {Soma_Tom} contra {Soma_Jim} de Jim.\n")

elif(Soma_Jim > Soma_Tom):
    print(f"Jim começa o jogo, pois a soma dos caracteres do seu nome deu {Soma_Jim} contra {Soma_Tom} de Tom.\n")

else:
    print(f"As somas dos caracteres foram iguais.\n")
    


print(ord('A'))
print(f"O valor de B é {ord('B')}")
print(f"O valor de C é {ord('C')}")
print(f"O valor de D é {ord('D')}")
print(f"O valor de b é {ord('b')}")
print(f"O valor de c é {ord('c')}")
print(f"O valor de d é {ord('d')}")
print(f"O valor de 0 é {ord('0')}")
print(f"O valor de 1 é {ord('1')}")
print(f"O valor de 2 é {ord('2')}")
print(f"O valor de * é {ord('*')}")
print(f"O valor de + é {ord('+')}")
print(f"O valor de (espaço ' ') é {ord(' ')}")

caracteres = ['A', 'B', 'C', 'D', 'b', 'c', 'd', '0', '1', '2', '*', '+', ' ']

for ch in caracteres:
    print(f"O valor de '{ch}' é {ord(ch)}")
