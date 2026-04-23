'''
Começo da Aula 7 (Aprendendo Python)
'''

# Funções
    # DRY - Don't repeat your self

def boas_vindas():
    print('Olá!')
    print('Seja bem vindo')

boas_vindas()

# Função com algoritmo
def somar_dois_numeros():
    numero1 = 10
    numero2= 5
    resultado1 = numero1 + numero2
    print(resultado1)

somar_dois_numeros()


# Funções
    # DRY - Don't repeat your self
    # Parametros --> argumentos

def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos', 5)
boas_vindas('Ronaldo', 4)
boas_vindas('Lisa', 2)


# Funções
    # DRY - Don't repeat your self
    # Parametros --> argumentos
    # Default = Aquele que você define o valor no parametro
    # Non-Default = Aquele que você não define o valor no parametro

def boas_vindas(nome , quantidade = 10):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos')



# Funções
    # DRY - Don't repeat your self
    # Ralizam uma tarefa
    # Calcula e retorna um valor

def cliente1(nome):
    print(f'Ola {nome}')

def cliente2(nome):
    return f'Ola {nome}'

x = cliente1('Maria')
y = cliente2('Jose')

print(x)
print(y)


# Funções
    # DRY - Don't repeat your self
    # Varios Argumentos (xargs)

# Criar uma função que soma varios numeros.

def soma(*numeros):
   resultado2 = 0
   for num in numeros:
        resultado2 += num
    #return resultado2



x = soma(2,3,4,7,4)

print(x)

'''
Fim da Aula 7
'''