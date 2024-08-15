N1 = int(input("Insira o primeiro numero: " ))
N2 = int(input("Insira o segundo numero: " ))

if (N1 == 0 & N2 == 0 | N2 == 0):
   print("ERRO DIVISAO POR ZERO, DELETANDO SYSTEM 32")
else:
   N3 = N1 / N2
   print(f"O resultado da divisao e: %.2f" % (N3))
   