# importando módulo math pra poder usar o valor exato de pi
import math

def rad_deg(angle_rad):
    # definindo o angulo em graus como aproximação de 1 casa decimal do angulo em rad vezes 180/pi
    angle_deg = round(angle_rad * (180 / math.pi), 1)
    return angle_deg

# recebendo o valor do angulo em rad como inteiro
angle_rad = int(input('Digite o angulo em radianos: '))

#imprimindo no console o angulo em graus
print(rad_deg(angle_rad))