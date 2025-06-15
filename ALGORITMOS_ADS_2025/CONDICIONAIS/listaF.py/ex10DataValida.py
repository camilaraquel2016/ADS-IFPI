from utils import entradaInt

def pedirDia():
    dia = entradaInt('Insira o dia: ')
    if dia >= 1 and dia <= 31:
        return dia
    else:
        print('Dia inválido, o dia precisa estar entre 1 e 31')
        return pedirDia()
    

def pedirMes():
    mes = entradaInt('Insira o mês: ')
    if mes >= 1 and mes <= 12:
        return mes
    else:
        print('Mês inválido, o mês precisa estar entre 1 e 12')
        return pedirMes()


def pedirAno():
    ano = entradaInt('Insira o ano: ')
    if ano >= 1000 and ano <= 9999:
        return ano
    else:
        print('Ano inválido, o ano deve ter 4 dígitos')
        return pedirAno()


def main():
    dia = pedirDia()
    mes = pedirMes()
    ano = pedirAno()

    print(f'{dia}/{mes}/{ano} é uma data válida!')
        
main()
