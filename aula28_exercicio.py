"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade')

if nome and idade != (''):
    print(f'{nome} Obrigado por digitar o seu nome')
    print(f'{nome}, seu nome invertido é', nome[::-1] )

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print('A primeira letra do seu nome é: ', nome[0])
    print(f'{nome}, A útima letra do seu nome é é', nome[-1] )
else:    
    print('Desculpe, você deixou campos vazios.')