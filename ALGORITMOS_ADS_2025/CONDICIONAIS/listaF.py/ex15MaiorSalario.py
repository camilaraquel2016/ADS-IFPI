from utils import entradaFloat, entradaInt

def calcularSalario(horasTrabalhadas: int, valorDaHora: float):
    return horasTrabalhadas * valorDaHora


def main():
    horasTrabalhadasProf1 = entradaInt('Horas aulas dadas pelo professor 1: ')
    valorHoraProf1 = entradaFloat('Valor da hora do professor 1: ')
    salarioProf1 = calcularSalario(horasTrabalhadasProf1, valorHoraProf1)

    
    horasTrabalhadasProf2 = entradaInt('Horas aulas dadas pelo professor 2: ')
    valorHoraProf2 = entradaFloat('Valor da hora do professor 2: ')
    salarioProf2 = calcularSalario(horasTrabalhadasProf2, valorHoraProf2)

    print(f'Salário professor 1: R${salarioProf1:.2f}\nSalário professor 2: R${salarioProf2:.2f}')

    if salarioProf1 > salarioProf2:
        print('Professor 1 tem o salário maior que o professor 2')
    elif salarioProf1 < salarioProf2:
        print('Professor 2 tem o salário maior que o professor 1') 
    else:
        print('Os dois professores tem salários iguais')


main()