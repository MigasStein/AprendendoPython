'''
Começo da Aula 6 Parte 2(Aprendendo Python)
'''

#
#
#
#For Loop - Criando um Retangulo

#Criar um retangulo 6x6

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end = '')
    print()

#
#
#
#Conhecendo o While Loop
print()
#Criar uma promoção para um produto de R$100.

valor = 100
dia = 0

while valor > 20:
    dia += 1
    print(f'No dia {dia} o produto cai ser vendido por R${valor}')
    valor -= 5

#
#
#
#Operador Ternário
print()
idade = 16

resultado = 'Voto Permitido' if idade >= 16 else 'Voto não Permitido'

print(resultado)

#
#
#
#Criando condições com While Loop


#Publicar um produto com comissao de 10% se for acima de R$20


valor = int(input('Digite o Valor do seu Produto: '))

while valor > 20:
    valor = (valor * 0.1) + valor
    print(f'O valor final do seu produto será de R${valor}')
    break

'''
Fim da Aula 6
'''