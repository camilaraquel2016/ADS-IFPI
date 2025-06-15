from utils import entradaFloat, validarLimiteMinFloat, entradaInt, validarNumLimiteInt

def converterCparaF(temperaturaC):
    return temperaturaC * 1.8 + 32


def converterCparaK(temperaturaC):
    return temperaturaC + 273.15


def converterFparaC(temperaturaF):
    return (temperaturaF - 32) * 5 / 9 


def converterFparaK(temperaturaF):
    return (temperaturaF + 459.67) * 5 / 9


def converterKparaC(temperaturaK):
    return temperaturaK - 273.15


def converterKparaF(temperaturaK):
    return (temperaturaK - 273.15) * 9 / 5 + 32


def pedirTemperaturaC():
    temperatura = entradaFloat('Digite a temperatura em C°: ')
    temperatura = validarLimiteMinFloat(temperatura, -273.15, 'Digite a temperatura em C°: ')
    return temperatura


def pedirTemperaturaK():
    temperatura = entradaFloat('Digite a temperatura em K°: ')
    temperatura = validarLimiteMinFloat(temperatura, 0, 'Digite a temperatura em K°: ')
    return temperatura


def pedirTemperaturaF():
    temperatura = entradaFloat('Digite a temperatura em F°: ')
    temperatura = validarLimiteMinFloat(temperatura, -459.67, 'Digite a temperatura em F°: ')
    return temperatura


def pedirEscolha():
    print('OPÇÃO 1: °C para °F\nOPÇÃO 2: °C para °K\nOPÇÃO 3: °F para °C\nOPÇÃO 4: °F para °K\nOPÇÃO 5: °K para °F\nOPÇÃO 6: °K para °C')
    escolha = entradaInt('Escolha uma opção (1 a 6): ')
    return validarNumLimiteInt(escolha, 1, 6, 'Escolha uma opção (1 a 6): ')


def converterTemperatura(escolha):
    if escolha == 1:
        temperaturaC = pedirTemperaturaC()
        temperaturaF = converterCparaF(temperaturaC)
        return f'{temperaturaC:.2f} °C = {temperaturaF:.2f} °F'
    
    if escolha == 2:
        temperaturaC = pedirTemperaturaC()
        temperaturaK = converterCparaK(temperaturaC)
        return f'{temperaturaC:.2f} °C = {temperaturaK:.2f} °K'
    
    if escolha == 3:
        temperaturaF = pedirTemperaturaF()
        temperaturaC = converterFparaC(temperaturaF)
        return f'{temperaturaF:.2f} °F = {temperaturaC:.2f} °C'
    
    if escolha == 4:
        temperaturaF = pedirTemperaturaF()
        temperaturaK = converterFparaK(temperaturaF)
        return f'{temperaturaF:.2f} °F = {temperaturaK:.2f} °K'
    
    if escolha == 5:
        temperaturaK = pedirTemperaturaK()
        temperaturaF = converterKparaF(temperaturaK)
        return f'{temperaturaK:.2f} °K = {temperaturaF:.2f} °F'
    
    if escolha == 6:
        temperaturaK = pedirTemperaturaK()
        temperaturaC = converterKparaC(temperaturaK)
        return f'{temperaturaK:.2f} °K = {temperaturaC:.2f} °C'
    

def main():
    print('-=' * 10 + 'CONVERSOR DE TEMPERATURA' + '-=' * 10)

    escolha = pedirEscolha()

    print(converterTemperatura(escolha))

main()    

    