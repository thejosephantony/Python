#  (Challenge: Fibonacci Sequence) In the Fibonacci sequence, each number is the
#  sum of the two preceding ones. The first 10 Fibonacci numbers are as follows:
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …
#  Write a script where a user inputs a position (a number) and the number in that position
#  in the Fibonacci Sequence is displayed.

anterior = 0
atual = 1
    
for i in range (10):
    print(anterior)
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    