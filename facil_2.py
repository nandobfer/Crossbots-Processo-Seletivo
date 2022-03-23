def conta_uns(num):
    uns = 0

    # converte decimal em string binary
    binary = bin(num)[2:]

    # percorre a string binary
    for i in binary:
        if i == '1':
            uns += 1
    return uns

num = int(input('Digite o número desejado: '))
print(conta_uns(num))