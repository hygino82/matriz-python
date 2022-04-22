from operator import truediv


def linha():
    print(40*'-')


def copiaMatriz(mat):
    matriz = []
    for i in range(len(mat)):
        linha = []
        for j in range(len(mat[0])):
            linha.append(mat[i][j])
        matriz.append(linha)
    return matriz


def verificaPossibilidadeProduto(ma, mb):
    la = len(ma)  # indica a quantidade de linhas de A
    ca = len(ma[0])  # indica a quantidade de colunas de A
    lb = len(mb)  # indica a quantidade de linhas de B
    cb = len(mb[0])  # indica a quantidade de colunas de B
    if(la != lb and ca != cb):
        return True
    else:
        return False


def verificaPossibilidadeSoma(ma, mb):
    la = len(ma)  # indica a quantidade de linhas de A
    ca = len(ma[0])  # indica a quantidade de colunas de A
    lb = len(mb)  # indica a quantidade de linhas de B
    cb = len(mb[0])  # indica a quantidade de colunas de B
    if(la != lb and ca != cb):
        return True
    else:
        return False


def verificaMatrizQuadrada(ma):
    la = len(ma)
    ca = len(ma[0])
    if (la == ca):
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
                elemento = ma[i][j] + mb[i][j]
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


def escalonamento(m):
    t = copiaMatriz(m)
    linhas = len(t)
    colunas = len(t[0])
    for p in range(linhas):
        if(t[p][p] == 0):
            for x in range(p+1, linhas, 1):
                for y in range(colunas):
                    t[p][y] += t[x][y]
        # não usei else pois dando certo ou não deverá ser executado a segunda condição
        if (t[p][p] != 0):
            for x in range(p+1, linhas, 1):
                cte = t[x][p] / t[p][p]

                for y in range(colunas):
                    t[x][y] = t[x][y] - cte * t[p][y]
    matriz = t[:]
    return matriz


def determinante(matriz):
    det = 1  # elemento neutro em um produto
    if(verificaMatrizQuadrada):
        for i in range(len(matriz)):
            det = det * matriz[i][i]
        return det
    else:
        return


t = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 2]]

print('\nMatriz T')
imprime(t)
linha()
if (verificaMatrizQuadrada):
    w = escalonamento(t)
    print('\nMatriz escalonada')
    imprime(w)
else:
    print('Erro ao realizar o procedimento')
linha()
print(f'Det = {determinante(w)}')


def matrizReduzida(mat, lx: int, cx: int):
    reduzida = []
    for i in range(len(mat)):
        linha = []
        if (i != lx):
            for j in range(len(mat[0])):
                if (j != cx):
                    linha.append(mat[i][j])
            reduzida.append(linha)
    return reduzida


print('Matriz reduzida [1,1]')
mr11 = matrizReduzida(t, 0, 0)
imprime(mr11)
