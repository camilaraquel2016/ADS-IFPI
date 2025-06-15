from itertools import count

def obter_qtd_dias(valor_emprestimo, taxa_diaria, valor_diario_pago):
    for dia in count():
        if valor_emprestimo <= 0:
            return dia 
        
        valor_emprestimo = valor_emprestimo - valor_diario_pago    
        valor_emprestimo = valor_emprestimo + (taxa_diaria * valor_emprestimo)
   

def main():
    taxa_diaria = 0.85 / 100
    valor_pago_diaramente = 200
    valor_emprestimo = 3000

    dias = obter_qtd_dias(valor_emprestimo, taxa_diaria, valor_pago_diaramente)
    print(f'São necessários {dias} dias para concluir o pagamento')

main()    
