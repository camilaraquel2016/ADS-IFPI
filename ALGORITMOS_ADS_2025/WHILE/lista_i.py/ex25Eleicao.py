from time import sleep

        
        
 

def menu():
    return f'1 - Canditado José\n2 - Canditado João\n3 - Canditado Joaquim\n9 - Nulo\n0 - Branco'


def obterVoto():
    print(menu())
    voto = int(input('Insira seu voto: '))

    while voto != 1 and voto != 2 and voto != 3 and voto != 9 and voto != 0:
        print('Voto inválido!')
        voto = int(input('Insira seu voto: '))

    return voto    


def apresentarResultado():
    qtdEleitores = 0
    resposta = 1
    votos1 = 0
    votos2 = 0
    votos3 = 0 
    votosBrancos = 0
    votosNulos = 0
    
    while resposta == 1:
        voto = obterVoto()
        qtdEleitores += 1

        match voto:
            case 1:
                votos1 += 1
            case 2: 
                votos2 += 1
            case 3:
                votos3 += 1
            case 9:
                votosNulos += 1
            case 0: 
                votosBrancos += 1

        resposta = int(input('Digite 1 para continuar ou qualquer número para sair: '))

    print('-=' * 10)
    print(f'Votos do canditado José: {votos1}\nVotos do canditado João: {votos2}\nVotos canditado Joaquim: {votos3}')   
    print(f'Votos Nulos: {votosNulos}\nVotos Brancos: {votosBrancos}') 
    print(f'Quantidade de eleitores: {qtdEleitores}')
    sleep(1)
    print('Carregando resultado...')
    sleep(1 )
    print('-=-Resultado 2025-=-')
    
    if votos1 > votos2 and votos1 > votos3:
        print('Vencedor: Canditado José')  
    elif votos2 > votos1 and votos2 > votos3:
        print('Vencedor: Canditado João')   
    elif votos2 > votos1 and votos2 > votos3:
        print('Vencedor: Canditado Joaquim')  
    else:
        print('Empate')      


def main():
    print('-=-ELEIÇÕES 2025-=-')

    apresentarResultado()


main()