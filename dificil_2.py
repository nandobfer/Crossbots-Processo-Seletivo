def newMatrix(N = 9): # função apenas para receber o sudoku do usuario
    matriz = []
    for i in range(N):
        linha = []
        for j in range(N):
            print('Insira o valor da linha', i+1, 'e coluna', j+1, ':')
            linha.append(input())
        matriz.append(linha)
    return matriz

def printSudoku(matriz): # função apenas para imprimir o sudoku
    for i in range(len(matriz)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - ')

        for j in range(len(matriz)):
            if j % 3 == 0 and j != 0:
                print('| ', end='')

            if j == 8:
                print(matriz[i][j])
            else:
                print(str(matriz[i][j]) + ' ', end='')
        print(matriz[i])

def getEmpty(matriz): # procura pelo proximo número 0 e retorna sua posição
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            if matriz[x][y] == 0:
                return (x,y)
    return None

def isValid(matriz, num, pos): # testa se o número atual é válido na configuração atual
    # checar linha
    for i in range(len(matriz)):
        if matriz[pos[0]][i] == num and pos[1] != i:
            return False
        #checar coluna
    for i in range(len(matriz)):
        if matriz[i][pos[1]] == num and pos[0] != i:
            return False

    #checar seção
    section = {
        'x': pos[1] // 3,
        'y': pos[0] // 3
    }
    for i in range(section['y']*3, section['y']*3 + 3):
        for j in range(section['x'] * 3, section['x'] * 3 + 3):
            if matriz[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(matriz): # solução baseada em backtracking, função testa cada número válido até chegar em uma posição sem solução, então ele volta uma solução e tenta novamente com o próximo número e assim por diante
    if not getEmpty(matriz): # se não houver espaço vazio, sudoku resolvido
        return True
    else:
        x,y = getEmpty(matriz) # caso contrário, salva a posição do espaço vazio

    for num in range(1, 10): # testar números de 1 a 9
        if isValid(matriz, num, (x,y)): # caso o número atual seja válido na posição atual
            matriz[x][y] = num # insere o número na posição atual, no sudoku

            if solve(matriz): # tenta o próximo espaço vazio
                return True
            matriz[x][y] = 0 # caso não haja solução, zera a posição atual e retorna falso pra chamada anterior repetir o processo
    return False

sudoku = newMatrix()
solve(sudoku)
printSudoku(sudoku)