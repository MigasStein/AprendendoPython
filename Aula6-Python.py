'''
Começo da Aula 6 (Aprendendo Python)
'''
#comparações condicionais

velocidade = 100

if velocidade > 110:
    print('Acima da Velocidade Permitida')    
    print('Favor Reduzir a Velocidade')
elif velocidade < 60:
    print('Favor dirigir acima de 80Km/h')
else:
    print('Velocidade OK')

#
#
#
#operadores logicos
print()

renda_acima_5mil = False
nome_limpo = True

#OR para que uma das condiçoes sejam aprovadas / AND as 2 condições tem que ser TRUE para estarem aprovadas

if renda_acima_5mil or nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento Negado')

#
#
#
#Multiplos operadores de comparação
print()

valor = 10

if 20<= valor < 40:
    print('Produto foi Aceito')
else:
    print('Produto não Aceito')

#
#
#
#For Loop - Utilizando números
print()

#imprimir de 1 a 5

for numero in range(1,11):
    print(numero)

#
#
#
#For Loop - Utilizando Strings
print()
palavra = 'Google'

for letra in palavra:
    print(f'{letra} esta dentro da palavra {palavra}')


#
#
#    
#For Loop - Utilizando If e Else

print()

compra_confirmada = True
dados_compra = 'Compra no valor de 12,50 e entrega confirmada'


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
        break
else:
    print('Falha na compra')

#
#
#
#For Loop - Nested loops
print()

for numero1 in range(1,6):
    print('Produto ' + str(numero1))
    for numero2 in range(11):
        print(numero1, numero2)
    
#
#
#
#For Loop - Separando Strings
print()
#Modificar de FANTASTICO para F A N T A S T I C O

palavra1 = 'FANTASTICO'

for spaco in palavra1:
    print(f'{spaco}' , end='')


'''
Fim da Aula 6
'''