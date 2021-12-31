import pandas as pandas
import random as random
import statistics as statistics
import collections as collections

planilha = pandas.read_excel("D:\Downloads\megaSenaResults.xlsx")
modaBola1 = statistics.mode(planilha['bola 1'])
modaBola2 = statistics.mode(planilha['bola 2'])
modaBola3 = statistics.mode(planilha['bola 3'])
modaBola4 = statistics.mode(planilha['bola 4'])
modaBola5 = statistics.mode(planilha['bola 5'])
modaBola6 = statistics.mode(planilha['bola 6'])

ocorrenciaBola1 = collections.Counter(planilha['bola 1'])
ocorrenciaBola2 = collections.Counter(planilha['bola 2'])
ocorrenciaBola3 = collections.Counter(planilha['bola 3'])
ocorrenciaBola4 = collections.Counter(planilha['bola 4'])
ocorrenciaBola5 = collections.Counter(planilha['bola 5'])
ocorrenciaBola6 = collections.Counter(planilha['bola 6'])

lista = list()
contador = 0
while True:
    num = random.randint(1, 60)
    if num not in lista:
        if num == modaBola1 or num == modaBola2 or num == modaBola3 or num == modaBola4 or num == modaBola5 or num == modaBola6:
            lista.append(num)
            contador += 1
    if contador >= 6:
        break    

lista.sort()
print(f"MODA - POR ORDEM DE BOLA {lista}")

lista.clear()

contador = 0
while True:
    num = random.randint(1, 60)
    if num not in lista:
        if contador == 0 and num == ocorrenciaBola1[0] or num == ocorrenciaBola1[1] or num == ocorrenciaBola1[2] or ocorrenciaBola1[3] or ocorrenciaBola1[num]:
            lista.append(num)
            contador += 1
        elif contador == 1 and num == ocorrenciaBola2[0] or num == ocorrenciaBola2[1] or num == ocorrenciaBola2[2] or ocorrenciaBola2[3] or ocorrenciaBola2[num]:
            lista.append(num)
            contador += 1
        elif contador == 2 and num == ocorrenciaBola3[0] or num == ocorrenciaBola3[1] or num == ocorrenciaBola3[2] or ocorrenciaBola3[3] or ocorrenciaBola3[num]:
            lista.append(num)
            contador += 1
        elif contador == 3 and num == ocorrenciaBola4[0] or num == ocorrenciaBola4[1] or num == ocorrenciaBola4[2] or ocorrenciaBola4[3] or ocorrenciaBola4[num]:
            lista.append(num)
            contador += 1
        elif contador == 4 and num == ocorrenciaBola5[0] or num == ocorrenciaBola5[1] or num == ocorrenciaBola5[2] or ocorrenciaBola5[3] or ocorrenciaBola5[num]:
            lista.append(num)
            contador += 1
        elif contador == 5 and num == ocorrenciaBola6[0] or num == ocorrenciaBola6[1] or num == ocorrenciaBola6[2] or ocorrenciaBola6[3] or ocorrenciaBola6[num]:
            lista.append(num)
            contador += 1
    if contador >= 6:
        break   

print(f'Sorteio ocorrência {lista}')
