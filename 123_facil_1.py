def repeat(item, n):
    lista = []
    for i in range(n):
      lista.append(item)

    return lista

item = input('Digite o nome do item: ')
n = int(input('Digite a quantidade de vezes que deseja repetir: '))

print(repeat(item, n))