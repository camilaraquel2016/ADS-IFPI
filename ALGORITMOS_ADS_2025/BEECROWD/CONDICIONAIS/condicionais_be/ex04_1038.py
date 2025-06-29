def obter_valor_unitario(codigo):
    if codigo == 1:
        return 4
    elif codigo == 2:
        return 4.5
    elif codigo == 3:
        return 5
    elif codigo == 4:
        return 2
    else:
        return 1.5
    

def main():
    valores = input().split()
    codigo = int(valores[0])
    qtd = int(valores[1])
    valor_unitario = obter_valor_unitario(codigo)
    valor_total = valor_unitario * qtd
    print(f'Total: R$ {valor_total:.2f}')

main()    
    