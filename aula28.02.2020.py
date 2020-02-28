'''
continua= True
while continua:
    try:
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    z= x/y
    print(x/y)
except ZeroDivisionError:
    print ('Opa, o segundo número não pode ser zero!')
except ValueError:
    print("O valor informado é de um tipo inválido!")
except Exception:
    print ('Algum outro erro ocorreu')
else:
print('Valores)
'''

'''

def funcao_1():
    print('Início da função 1')
    funcao_2()
    print('Fim da função 1')


def funcao_2():
    print('Início da função 2')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(15):
        try:
            print(lista[i]) 
        except IndexError:
            print('Indice inexistente')
    print('Fim da função 2')


print('Início do programa')
funcao_1()
print('Fim do programa')


'''


'''def inserir_nome(lista_nomes, nome):
    lista_nomes.append(nome)


def busca_nome(lista_nomes, indice):
    try:
        if indice >= len(lista_nomes):
            raise IndexError
    except IndexError:
        return 'Indice inexistente'
    else:
        return lista_nomes [indice]



lista_nomes = []
inserir_nome(lista_nomes, 'Paulo')
inserir_nome(lista_nomes,'João')
nome = busca_nome (lista_nomes,1)
print(nome)
'''

alunos={}


def inserir_aluno (alunos, RA, nome):
    alunos[nome]=[RA]

for i in range (3):
    nome=input("Nome:")
    RA=input("RA: ")
    inserir_aluno(alunos, nome, RA)


print (alunos)