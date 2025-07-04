def obter_movimentos(qtd_movimentos):
    movimentos = []

    for entrada in range(qtd_movimentos):
        movimento = int(input())
        movimentos.append(movimento)

    return movimentos    


def obter_status_de_cada_copo(posicao_inicial_da_moeda, copos):
    status_copos = []

    for copo in copos:
        if copo == posicao_inicial_da_moeda:
            copo = True
        else:
            copo = False
        status_copos.append(copo)        

    return status_copos    


def atualizar_status(status_de_cada_copo, num_do_movimento):
    a, b, c = status_de_cada_copo
    if num_do_movimento == 1:
        a, b = b, a
    elif num_do_movimento == 2:
        b, c = c, b  
    else:
       a, c = c, a 

    return [a, b, c]  


def obter_posicao_final_da_moeda(movimentos, posicao_inicial_da_moeda, copos):
    status_de_cada_copo = obter_status_de_cada_copo(posicao_inicial_da_moeda, copos)
    
    for num_do_movimento in movimentos:
        status_de_cada_copo = atualizar_status(status_de_cada_copo, num_do_movimento)

    contador = 0

    for index in status_de_cada_copo:
        if index == True:
            return copos[contador]
        
        contador += 1


def main():
    copos = ['A', 'B', 'C']
    qtd_movimentos = int(input())
    posicao_inicial_da_moeda = input()
    movimentos = obter_movimentos(qtd_movimentos)
    posicao_final_da_moeda = obter_posicao_final_da_moeda(movimentos, posicao_inicial_da_moeda, copos)
    print(posicao_final_da_moeda)

main()   
    


