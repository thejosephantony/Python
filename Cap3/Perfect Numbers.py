#  (Perfect Numbers) In number theory, a perfect number is a positive integer that is
#  equal to the sum of its divisors. Perfect numbers were first studied by the Pythagoreans
#  who thought that they had mystical properties. They were also extensively studied by
#  Greeks (including Euclid) for their numerological properties.
#  The smallest perfect number is 6, because 6 = 3 + 2 + 1, with 3, 2, and 1 being the divi
# sors. Other examples of perfect numbers are: 28, 496 and 8128. Write a script that inputs
#  a nonnegative integer and displays whether it is a perfect number or not

num = int(input("Informe o número: \n"))
if(num < 0):
    print(f"O número {num} é negativo\n")
else:
    soma = 0
    
    for i in range(1, num):
        if(num % i == 0):
            soma = soma + i
            
    if(soma == num):
        print(f"O número {num} é perfeito.\n")
    else:
        print(f"O número {num} não é perfeito.\n")