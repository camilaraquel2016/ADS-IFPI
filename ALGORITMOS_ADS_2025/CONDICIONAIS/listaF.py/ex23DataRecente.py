from utils import entradaInt

def pedirDia():
    dia = entradaInt('Insira o dia: ')

    if dia >= 1 and dia <= 31:
        return dia
    else:
        print('Dia inválido!\nO dia precisa estar entre 1 e 31')
        return pedirDia()


def pedirMes():
    mes = entradaInt('Insira o mês: ')

    if mes >= 1 and mes <= 12:
        return mes
    else:
        print('Mês inválido!\nO mês precisa estar entre 1 e 12')
        return pedirMes()


def pedirAno():
    ano = entradaInt('Insira o ano: ')

    if ano >= 1000 and ano <= 9999:
        return ano
    else:
        print('O ano precisa estar entre 1000 e 9999')
        return pedirAno()
    

def dataRecente(dia1, mes1, ano1, dia2, mes2, ano2):
    data1 = f'{dia1}/{mes1}/{ano1}'
    data2 = f'{dia2}/{mes2}/{ano2}'

    if ano1 > ano2:
        return data1
    elif ano2 > ano1:
        return data2
    else:
        if mes1 > mes2:
            return data1
        elif mes2 > mes1:
            return data2
        else:
            if dia1 > dia2:
                return data1
            elif dia2 > dia1:
                return data2
            else:
                return 'Datas iguais'
            
    

def main():
    print('-=-PRIMEIRA DATA-=-')

    dia1 = pedirDia()
    mes1 = pedirMes()
    ano1 = pedirAno()

    print('-=-SEGUNDA DATA-=-')

    dia2 = pedirDia()
    mes2 = pedirMes()
    ano2 = pedirAno()   

    dataMaisRecente = dataRecente(dia1, mes1, ano1, dia2, mes2, ano2)

    print('-=-=-=-=-=-=-=')

    print(f'Data mais recente: {dataMaisRecente}')


main()    
    


