"""
Considerando duas listas de inteiros ou floats ( lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a  =[1, 2, 3, 4, 5, 6, 7]
lista_b  =[1, 2, 3, 4]

=============== resultado
lista_soma  =[2, 4, 6, 8]
"""

lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

lista_soma = [x + y for x, y in zip(lista1, lista2)] # soma cada tupla formada com o uso do zip
print (lista_soma)

#--- ou com import ---#

from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]

#--- uso para qualque linguagem ---#

lista_vazia = []
for i in range(len(lista2)): #uso como parametro de parada o tamanho da lista 2
    lista_vazia.append(lista1[i] + lista2[i]) # adiciona os valores na lista vazia e vai somando
print(lista_vazia)