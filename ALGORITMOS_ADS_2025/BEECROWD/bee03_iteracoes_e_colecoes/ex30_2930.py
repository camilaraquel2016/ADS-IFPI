def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao   


def exibir_msg(diferenca_dias, dia_final):
    if diferenca_dias >= 3:
        print('Muito bem! Apresenta antes do Natal!')
    else:
        print('Parece o trabalho do meu filho!')
        dia_final += 2
        if dia_final > 24:
            print('Fail! Entao eh nataaaaal!')
        else:
            print('TCC Apresentado!')        
        

def main():
    e, d = mapear(input().split(), int)
    if e > d:
        print('Eu odeio a professora!')
    else:
        diferenca_dias = d - e
        exibir_msg(diferenca_dias, d)

main()    



