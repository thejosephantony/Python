#  2.4(Arithmetic) Test each of the arithmetic operators +, -, *, /, // and ** with -5, 0, 5, and 7.5 as the left operand and 2 as the right operand. 

valores = [-5, 0, 5, 7.5]
constante = 2

for valor in valores:
    soma = valor + constante
    subtracao = valor - constante
    multiplicacao = valor * constante
    divisao = valor / constante
    divisao_inteira = valor // constante
    exponenciacao = valor ** constante
    print(f"Operacoes com {valor} e {constante}:")
    print(f"  Soma: {valor} + {constante} = {soma}")
    print(f"  Subtracao: {valor} - {constante} = {subtracao}")
    print(f"  Multiplicacao: {valor} * {constante} = {multiplicacao}")
    print(f"  Divisao: {valor} / {constante} = {divisao}")
    print(f"  Divisao Inteira: {valor} // {constante} = {divisao_inteira}")
    print(f"  Exponenciacao: {valor} ** {constante} =   {exponenciacao}")   
