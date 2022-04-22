from operator import truediv


def linha():
    print(40*'-')


def verificaPossibilidadeproduto(ma, mb):
    la = len(ma)  # indica a quantidade de linhas de A
    ca = len(ma[0])  # indica a quantidade de colunas de A
    lb = len(mb)  # indica a quantidade de linhas de B
    cb = len(mb[0])  # indica a quantidade de colunas de B
    if(la != lb and ca != cb):
        return True
    else:
        return False


def abrirMatriz(arq: str):
    arquivo = open(arq, "r")
    matriz = []

    linha = arquivo.readline()
    while(linha != ""):
        elementos = linha.split(' ')
        for n in range(len(elementos)):
            elementos[n] = float(elementos[n])
        matriz.append(elementos)
    arquivo.close()
    return matriz


def entradaMatriz():
    l = int(input('Informe o número de linhas'))
    c = int(input('Informe o número de colunas'))
    matriz = []

    for i in range(l):
        linha = []
        for j in range(c):
            valor = float(
                input(f'Informe o elemento da linha {i} e coluna {j} -> '))
            linha.append(valor)
        matriz.append(linha)

    print('Dados da matriz inseridos com sucesso!')
    return matriz


def imprime(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], ' ', end='')
        print()


def imprimeTransposta(matriz):
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            print(matriz[i][j], ' ', end='')
        print()


def matrizEscalar(valor: float, mat):
    matriz = []
    for i in range(len(mat)):
        linha = []
        for j in range(len(mat[0])):
            linha.append(valor * mat[i][j])
        matriz.append(linha)
    return matriz


def matrizSoma(ma, mb):
    la = len(ma)  # indica a quantidade de linhas de A
    ca = len(ma[0])  # indica a quantidade de colunas de A
    lb = len(mb)  # indica a quantidade de linhas de B
    cb = len(mb[0])  # indica a quantidade de colunas de B
    if(la != lb and ca != cb):
        print('Não é possivel somar as matrizes,\npois suas dimensões são incompatíveis.')
        return
    else:
        print('Podemos somar as matrizes.')
        matriz = []
        for i in range(la):
            linha = []
            for j in range(cb):
                elemento = ma[i][j]+mb[i][j]
                linha.append(elemento)
            matriz.append(linha)
        return matriz


def matrizProduto(ma, mb):
    la = len(ma)  # indica a quantidade de linhas de A
    ca = len(ma[0])  # indica a quantidade de colunas de A
    lb = len(mb)  # indica a quantidade de linhas de B
    cb = len(mb[0])  # indica a quantidade de colunas de B
    if(ca != lb):
        print('Não é possivel somar as matrizes,\npois suas dimensões são incompatíveis.')
        return
    else:
        matriz = []
        for i in range(la):
            linha = []
            for j in range(cb):
                elemento = 0
                for k in range(ca):
                    elemento += ma[i][k] * mb[k][j]
                linha.append(elemento)
            matriz.append(linha)
    return matriz

# a = [[2, 3, 4],
#      [5, 6, 7]]

# b = [[-1, 3.5, 9],
#      [8, 2, 3]]

# print('Matriz A')
# imprime(a)
# print('Matriz B')
# imprime(b)
# c = matrizSoma(a, b)
# print('Matriz soma')
# imprime(c)


d = [[5, 2],
     [3, 7]]

e = [[9, 5],
     [1, 3]]

print('Matriz D')
imprime(d)
linha()
print('Matriz E')
imprime(e)
linha()
if (verificaPossibilidadeproduto(d, e)):
    print('Matriz do produto CxD')
    prod_cd = matrizProduto(d, e)
    imprime(prod_cd)
else:
    print('Não é possivel somar as matrizes,\npois suas dimensões são incompatíveis.')
