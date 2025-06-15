from utils import entradaInt, validarLimiteMinInt

def parOuImpar(num):
   if num % 2 == 0:
      return 'pares'
   else:
      return 'ímpares'


def decisao(n1, n2):
    n2 = validarLimiteMinInt(n2, 1, 'Insira o segundo número: ')
    restoDivisao = n1 % n2      

    match restoDivisao:
        case 1:
          resultado = n1 + n2 + restoDivisao
          return f'{n1} + {n2} + {restoDivisao} = {resultado}'
       
        case 2:
          resParImpar = parOuImpar(n1) # quando o resto da divisão é 2, fica subtendido que o divisor e o dividendo possuem a mesma propriedade (ser par ou ímpar) logo basta usar apenas um como paramêtro para analisar se eles são pares ou ímpares
          return f'São {resParImpar}'
       
        case 3:
          resultado =  (n1 + n2) * n1
          return f'({n1} + {n2}) * {n1} = {resultado }'
       
        case 4:
          resultado = (n1 + n2) / n2
          return f'({n1} + {n2}) / {n2}  = {resultado:.2f}'
          
        case _:
          quadradoDeN1 = n1 ** 2
          quadradoDeN2 = n2 ** 2
          return f' \nQuadrado de {n1} = {quadradoDeN1}\nQuadrado de {n2} = {quadradoDeN2}' 
       

def main():
   n1 = entradaInt('Insira o primeiro número: ')
   n2 = entradaInt('Insira o segundo número: ')

   res = decisao(n1, n2)

   print(f'Resultado: {res}')       


main()   