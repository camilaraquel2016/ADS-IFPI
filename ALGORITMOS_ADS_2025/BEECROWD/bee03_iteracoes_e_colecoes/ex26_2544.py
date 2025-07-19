def obter_qtd_vezes(num):
    qtd_vezes = 0 

    while num > 1:
        num = num / 2
        qtd_vezes += 1

    return qtd_vezes    


def main():
    try:
        while True:
            n = int(input())
            if not n:
                break
            print(obter_qtd_vezes(n))
    except (EOFError, ValueError):
        pass        

main()    