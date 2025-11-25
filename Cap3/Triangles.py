#  (Triangles) In an equilateral triangle, the lengths of all three sides are equal. Con
# sequently, it is also equiangular with all three internal angles congruent to each other and
#  measuring 60°. Write a script where a user can input the length of the three sides of a tri
# angle. The script should determine if it is an equilateral triangle or not.


lado1 = int(input("Insira o 1º lado do triângulo: \n"))
lado2 = int(input("Insira o 2º lado do triângulo: \n"))
lado3 = int(input("Insira o 3º lado do triângulo: \n"))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    
    if(lado1 == lado2 == lado3):
        print("O triângulo é equilátero\n")
    else:   
        print("Os lados não formam um triângulo equilátero\n")
    
else:
    print("Os lados não formam um triângulo.\n")
