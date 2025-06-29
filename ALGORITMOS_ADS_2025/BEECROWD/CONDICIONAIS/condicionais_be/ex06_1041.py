def obter_localizacao(eixo_x, eixo_y):
    if eixo_x == 0 and eixo_y == 0:
        return 'Origem'
    elif eixo_x > 0 and eixo_y > 0:
        return 'Q1'
    elif eixo_x < 0 and eixo_y > 0:
        return 'Q2'
    elif eixo_x < 0 and eixo_y < 0:
        return 'Q3'
    elif eixo_x > 0 and eixo_y < 0:
        return 'Q4'
    elif eixo_x == 0 and eixo_y != 0:
        return 'Eixo Y'
    elif eixo_y == 0 and eixo_x != 0:
        return 'Eixo X'
    

def main():
    eixos = input().split()

    eixo_x = float(eixos[0]) 
    eixo_y = float(eixos[1])

    localizacao = obter_localizacao(eixo_x, eixo_y)

    print(localizacao)

main()       
