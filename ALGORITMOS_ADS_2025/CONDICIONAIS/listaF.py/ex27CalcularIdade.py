from utils import entradaInt, pedirDia, pedirMes, pedirAno

def calcularIdade(diaAtual, mesAtual, anoAtual, diaNasc, mesNasc, anoNasc):
    quantDiasAtual = diaAtual + mesAtual * 30 + anoAtual * 365
    quantDiasNasc = diaNasc + mesNasc * 30 + anoNasc * 365

    idadeDias = quantDiasAtual - quantDiasNasc
    print(idadeDias)

    anosIdade = idadeDias // 365
    mesesIdade = idadeDias % 365 // 30
    diasIdade = idadeDias % 360

    return f'Idade: {diasIdade} dia(s), {mesesIdade} mes(es) e {anosIdade} ano(s)'
    

def main():
    print('-=-Descobrindo idade-=-')


    print('-=-Data atual-=-')
    diaAtual = pedirDia()
    mesAtual = pedirMes()
    anoAtual = pedirAno()

    print('-=-Data nascimento-=-')
    diaNasc = pedirDia()
    mesNasc = pedirMes()
    anoNasc = pedirAno()

    idade = calcularIdade(diaAtual, mesAtual, anoAtual, diaNasc, mesNasc, anoNasc)

    print(idade)


main()    