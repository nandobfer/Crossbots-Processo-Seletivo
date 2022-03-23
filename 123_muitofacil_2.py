def convert(hour):
    min = hour * 60
    seg = min * 60
    mili = seg * 1000

    sem = int(hour / (24 * 7))
    mes = int(hour / (24 * 30))

    lista = [mes, sem, min, seg, mili]
    return lista

num = int(input('Digite o número de horas: '))

print(convert(num))

