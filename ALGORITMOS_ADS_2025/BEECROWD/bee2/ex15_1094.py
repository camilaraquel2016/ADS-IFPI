def saida(c, r, s, total):
    print(f'Total: {total} cobaias')
    print(f'Total de coelhos: {c}')
    print(f'Total de ratos: {r}')
    print(f'Total de sapos: {s}')
    print(f'Percentual de coelhos: {c / total * 100:.2f} %')
    print(f'Percentual de ratos: {r / total * 100:.2f} %')
    print(f'Percentual de sapos: {s / total * 100:.2f} %')


def obter_resultados(qtd_entradas):
    c, r, s, total = 0, 0, 0, 0

    for _ in range(qtd_entradas):
        entrada = input().split()
        qtd = int(entrada[0])
        tipo = entrada[1]

        if tipo == 'C':
            c += qtd
        elif tipo == 'R':
            r += qtd
        else:
            s += qtd

        total += qtd    

    return c, r, s, total


def main():
    qtd_entradas = int(input())
    resultados = obter_resultados(qtd_entradas)
    c, r, s, total = resultados
    saida(c, r, s, total)

main()    
