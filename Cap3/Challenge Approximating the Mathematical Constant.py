#  (Challenge: Approximating the Mathematical Constant ) Write a script that com
# putes the value of π from the following infinite series. Print a table that shows the value of
#  π approximated by one term of this series, by two terms, by three terms, and so on. How
#  many terms of this series do you have to use before you first get 3.14? 3.141? 3.1415?
#  3.14159?

soma = 0
alvo_2 = None   # 3.14
alvo_3 = None   # 3.141
alvo_4 = None   # 3.1415
alvo_5 = None   # 3.14159

print("n   aproximação de pi")

for n in range(1, 500000):
    termo = ((-1)**(n-1)) / (2*n - 1)
    soma += termo
    pi_aprox = 4 * soma

    # aqui mostrar os primeiros 10
    if n <= 10:
        print(f"{n:2d}  {pi_aprox:.12f}")

    # vai verificar metas
    if alvo_2 is None and format(pi_aprox, ".2f") == "3.14":
        alvo_2 = n
    if alvo_3 is None and format(pi_aprox, ".3f") == "3.141":
        alvo_3 = n
    if alvo_4 is None and format(pi_aprox, ".4f") == "3.1415":
        alvo_4 = n
    if alvo_5 is None and format(pi_aprox, ".5f") == "3.14159":
        alvo_5 = n

    # parar quando achar tudo
    if alvo_2 and alvo_3 and alvo_4 and alvo_5:
        break

print("\nPrimeiro n que alcança cada precisão:")
print("3.14    →", alvo_2)
print("3.141   →", alvo_3)
print("3.1415  →", alvo_4)
print("3.14159 →", alvo_5)
