# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:30:01 2024

@author: ryanm
"""

def clear():
    linhas = 130
    print("\n" * linhas)
    
fib : int
val : int

aux1 = 0
aux2 = 1
contador = 1
fib = 1
val = int(input("insira o valor do fibonnaci que deseja calcular: "))


#A sequência de Fibonacci é uma sequência de números, onde cada número é a soma dos 2 números anteriores, 
#exceto os dois primeiros números que são 0 e 1.
if(val >= 1):
    clear()
    print(f"Os numero {val} da sequencia de Fibonnaci são: ")
    
while (contador <= val ):
    
    print(f"fib: {fib}")
    fib = aux1 + aux2
    aux1 = aux2
    aux2 = fib
    contador += 1
    
        



