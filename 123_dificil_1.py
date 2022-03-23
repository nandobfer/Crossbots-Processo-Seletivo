# funcao apenas pra receber a matriz do usuario inicializando a matriz como uma lista (colunas) e 
# inserindo uma nova lista (linhas) pra cada indice da lista matriz e recebendo do usuario o valor
# de cada indice da lista linha
def newMatrix(N):
    matriz = []
    for i in range(N):
        linha = []
        for j in range(N):
            print('Insira o valor da linha', i+1, 'e coluna', j+1, ':')
            linha.append(input())
        matriz.append(linha)
    return matriz

# inicializando uma lista para casas visitadas e outra para fila, solução baseada no Breadth First Search
visited = [[0,0]]
queue = [[0,0]]

def bfs(visited, queue, matriz, N):

    ways = {} #inicializando um dictionary que armazenará as posições adjacentes de cada posição

    while queue: #repetir enquanto houver algo na lista queue
        pos = queue.pop(0) # inicializando variavel que simboliza a posição atual da comitiva e remove ela da fila
        x = 1
        y = 1
        for i in range(2): # testando se a direita (+x) ou esquerda (-x) são montanhas ou precipicios
            next_pos = pos[:] # definindo a nova posição como uma copia da original
            next_pos[1] += x # andando uma casa em x
            x = -x
            if next_pos[1] < N and next_pos[1] > 0: # caso a proxima posição esteja dentro dos limites da matriz
                if matriz[next_pos[0]][next_pos[1]] == 'M' and not next_pos in visited: # caso a proxima posição seja montanha e ainda não tenha sido visitada
                    queue.append(next_pos) # adiciona a posição nova na fila
                    visited.append(next_pos) # adiciona a posição nova na lista de posições já visitadas
                    ways[tuple(next_pos)] = tuple(pos) # salvando essa posição como uma posição adjacente possível da anterior, função tuple pois listas não são indexáveis e será necessário indexar a frente
            else:
                continue # caso contrário, não faz nada e passa pra proxima posição

        for i in range(2): # repete tudo anterior, só que na direção y
            next_pos = pos[:]
            next_pos[0] += y
            y = -y
            if next_pos[0] < N and next_pos[0] > 0:
                if matriz[next_pos[0]][next_pos[1]] == 'M' and not next_pos in visited:
                    queue.append(next_pos)
                    visited.append(next_pos)
                    ways[tuple(next_pos)] = tuple(pos)
            else:
                continue

    shortest_way = {} # inicializando um novo dictionary que será o caminho mais curto
    position = (N-1, N-1) # inicializando uma variavel na posição final do mapa
    if position in ways: # se houver uma posição final nos caminhos, significando que há solução
        while position != (0,0): # repete até posição ser igual o início
            shortest_way[ways[position]] = position # faz o caminho contrário
            position = ways[position]
        return len(shortest_way) # retorna o tamanho do dict, que é a quantidade de casas do caminho mais curto
    else:
        return 'SI' # caso não haja solução

N = int(input('Digite o tamanho da matriz: '))
print('Movimentos necessários:', bfs(visited, queue, newMatrix(N), N))