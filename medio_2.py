# definindo funções que retornam True caso o número seja múltiplo de 3 e 5, respectivamente
def mult_3(num):
    if (num % 3) == 0:
        return True

def mult_5(num):
    if (num % 5) == 0:
        return True

def crossbots(num):
    # checa se ambas funções retornam True, caso contrário, checa cada uma
    if mult_3(num) and mult_5(num):
        return 'CrossBots'
    elif mult_3(num):
        return 'Cross'
    elif mult_5(num):
        return 'Bots'
    else:
        return num

num = int(input('Digite o número: '))

print(crossbots(num))