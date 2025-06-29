def obter_index_valido(n, index_da_cidade_a_ser_apagada):
    ultimo_index = n - 1
    if index_da_cidade_a_ser_apagada > ultimo_index:
        index_da_cidade_a_ser_apagada -= ultimo_index

    return index_da_cidade_a_ser_apagada    


def obter_num_da_ultima_regiao(n, m, regioes):

    print(regioes)
    


    index_da_cidade_a_ser_apagada = 0
    regioes[0] = 0

    for i in range(5):
        print(regioes)
        index_da_cidade_a_ser_apagada += 3
        index_da_cidade_a_ser_apagada = obter_index_valido(n, index_da_cidade_a_ser_apagada)
        

        while regioes[index_da_cidade_a_ser_apagada] == 0:
            index_da_cidade_a_ser_apagada += 1


        regioes[index_da_cidade_a_ser_apagada] = 0
        



 
    



# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 
#1 2 3 4 5 6 7 
#0 2 0 0 0 0 0 

# 0, 3, 6, 4, 2, 5



def obter_regioes(n):
    regioes = []

    for regiao in range(n):
        regioes.append(regiao + 1)

    return regioes    



def main():
    n = int(input())
    regioes = obter_regioes(n)
    m = 3
    obter_num_da_ultima_regiao(n, m, regioes)
    

main()    
      