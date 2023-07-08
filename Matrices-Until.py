matriz_ganho = []
lista_ganho = []
lista_mes = []
ganho = 1
while ganho != 0:
    mes = str(input("Insira o mês de referência: "))
    ganho = float(input("Insira o ganho referênte ao mês: "))
    linha=[mes,ganho]
    matriz_ganho.append(linha)
    lista_ganho.append(ganho)
    lista_mes.append(mes)
if ganho == 0 :
    print(matriz_ganho)
maiorqntd = 0.1
mes = ""
for linha in matriz_ganho:
    if linha[1] > maiorqntd:
        maiorqntd = linha[1]
        mes = linha [0]
soma = 0
for total in lista_ganho:
    soma = soma + total       
media = soma/len(matriz_ganho)
print(mes,"obteve o maior ganho com ",maiorqntd,"R$")
print("O total ganho no intervalo informado foi de ",soma,"R$")
if len(matriz_ganho) > 1:
    print("Foram informados",len(matriz_ganho),"meses.")
else:
    print("Informado apenas",len(matriz_ganho),"mes.")
print("Média de ganhos no intervalo : ",media)     
