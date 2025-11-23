# w = o(1 + p)n
#  where
#  w is the new hourly wage,
#  o is the original hourly wage,
#  p is the percentage increase or decrease, and
#  n is the number of years with an increase or decrease in hourly wage.

salario_inicial = 10
anos_aumento = 5
anos_reducao = 2
percentual_aumento = 0.03
percentual_reducao = 0.03

print(f"O novo salário após cinco anos de avaliações boas é: US${(salario_inicial*(1 + percentual_aumento)**anos_aumento):.2f}")
print(f"O novo salário após dois anos de avaliações ruins é: US${(salario_inicial*(1 - percentual_reducao)**anos_reducao):.2f}")



