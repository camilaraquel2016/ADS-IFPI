def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao


def obter_localizacao(n, m, x, y):
    if x == n or y == m:
        return 'divisa'
    elif x > n and y > m:
        return 'NE'
    elif x < n and y > m:
        return 'NO'
    elif x < n and y < m:
        return 'SO'
    elif x > n and y < m:
        return 'SE'


def repetir(num_consultas):
    n, m = mapear(input().split(), int)

    for consulta in range(num_consultas):
        x, y = mapear(input().split(), int)
        localizacao = obter_localizacao(n, m, x, y)
        print(localizacao)


def main():
    while True:
        num_consultas = int(input())
        if num_consultas == 0:
            break
         
        repetir(num_consultas)

main() 

   
