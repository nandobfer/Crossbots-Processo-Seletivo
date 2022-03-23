# importando módulo math para usar a função que sqrt que retorna a raiz quadrada do argumento
import math

def dist(A, B):
    # aplicando teorema de pitagoras
    comprimento = math.sqrt(((B['x'] - A['x'])**2) + ((B['y'] - A['y'])**2))
    return round(comprimento, 2)

# definindo os pontos A e B como dicionarios para facilitar interpretação cartesiana
A = {
    'x': int(input('Digite a coordenada X do ponto A: ')),
    'y': int(input('Digite a coordenada Y do ponto A: '))
}
B = {
    'x': int(input('Digite a coordenada X do ponto B: ')),
    'y': int(input('Digite a coordenada Y do ponto B: '))
}

print(dist(A, B))