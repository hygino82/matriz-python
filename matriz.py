def entradaMatriz():
    l = int(input('Informe o número de linhas'))
    c = int(input('Informe o número de colunas'))
    matriz = []

    for i in range(l):
        linha = []
        for j in range(c):
            valor = float(
                input(f'Informe o elemento da linha {i} e coluna {j}'))
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
    lb = len(ma)  # indica a quantidade de linhas de B
    cb = len(ma[0])  # indica a quantidade de colunas de B
    if(la != lb and ca != cb):
        print('Não é possivel somar as matrizes,\npois suas dimensões são incompatíveis.')
    else:
        print('Podemos somar as matrizes.')


a = [[2, 3, 4],
     [5, 6, 7]]

b = matrizEscalar(3, a)
print('Matriz B')
imprime(b)

matrizSoma(a, b)  # Não implementado completamente ainda
t = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 2]]
