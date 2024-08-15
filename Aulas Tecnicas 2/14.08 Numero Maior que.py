# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:05:56 2024

@author: ryanm
"""

A = int(input("Insira o Primeiro numero: \n"))
B = int(input("Insira o Segundo numero: \n"))
C = int(input("Insira o Terceiro numero: \n"))

Maior = 0
Menor = 0
Meio = 0

if (A > B and A > C):
    Maior = A
elif( A < B and A < C):
    Menor = A
    
if(B > A and B > C):
    Maior = B        
elif( B < A and B < C):
    Menor = B

if (C > B and C > A):
    Maior = C    
elif( C < B and C < A):
    Menor = C

if (B == C):
    print("C e B sao iguais")

if (A == B):
    print("A e B sao iguais")

if (C == A):
    print("A e C sao iguais")
    
if (C < A and C > B):
    print("C e o numero do meio")
elif (B > C and B < A):
    print("B e o numero do meio")
elif (A > B and A < C):
    print("A e o numero do meio")



if(Maior == 0 and Meio == 0 and Menor == 0):
    print("Todos os numeros sao iguais\n")
else:
    print("O maior e %d" % Maior + " E o menor %d" % Menor)