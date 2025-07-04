def obter_maior(n1, n2):
    return n1 if n1 > n2 else n2


def reduzir(colecao, funcao_redutora, valor_inicial):
    acumulado = valor_inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado
    

def obter_ordem_decrescente(colecao):
    nova_ordem = []

    for i in range(len(colecao)):
        maior = reduzir(colecao, obter_maior, colecao[0])
        nova_ordem.append(maior)
        colecao.remove(maior)

    return nova_ordem    

    
def obter_qtd_de_blocos(tipos_em_ordem_decrescente, tamanho_orginal):
    qtd_blocos = 0

    for tamanho_tipo in tipos_em_ordem_decrescente:
        qtd_blocos += tamanho_orginal // tamanho_tipo
        tamanho_orginal = tamanho_orginal % tamanho_tipo

        if tamanho_orginal == 0:
            return qtd_blocos


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao    


def repetir(qtd_casos):
    for caso in range(qtd_casos):
        qtd_tipos, tamanho_bloco = mapear(input().split(), int)
        tipos = mapear(input().split(), int)
        tipos_em_ordem_decrescente = obter_ordem_decrescente(tipos)
        qtd_blocos = obter_qtd_de_blocos(tipos_em_ordem_decrescente, tamanho_bloco)
        print(qtd_blocos)


def main():
    qtd_casos = int(input())
    repetir(qtd_casos)
    
main()    
