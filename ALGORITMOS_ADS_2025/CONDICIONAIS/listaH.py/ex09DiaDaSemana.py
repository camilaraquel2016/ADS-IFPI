def obterDiaDaSemana(opcao: int): 
    if opcao == 1:
        return 'Domingo'
    if opcao == 2:
        return 'Segunda'
    if opcao == 3:
        return 'Terça'
    if opcao == 4:
        return 'Quarta'
    if opcao == 5:
        return 'Quinta'
    if opcao == 6:
        return 'Sexta'
    if opcao == 7:
        return 'Sábado'
   
    

def main():
    opcao = int(input('Digite sua opção: '))
    if obterDiaDaSemana(opcao):
        diaDaSemana = obterDiaDaSemana(opcao)
        print(f'Hoje é {diaDaSemana}')
    else:
        print('Opção inváida')    

main()    
    


