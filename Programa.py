from operacoes.matriz import *

k = [[1, 2],
     [3, 4]]

linha()
print('Matriz K')
imprime(k)
print(f'Determinante = {determinante(k)}')
print('Inversa de K')
inv_k = matrizInversa(k)
imprime(inv_k)
