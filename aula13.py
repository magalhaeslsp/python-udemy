nome = 'Lucas Magalhães'
altura = 1.80
peso = 100
imc = peso / (altura * altura) # IMC = peso (kg)/[altura x altura (m)

# formatação de variavel

linha_1 = f'O {nome} tem {altura:.3f} de altura,' # manipulando quantas casas decimais eu quero 
linha_2 = f'pesa {peso} quilos e seu IMC é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)


# Uma introdução às f-strings (formatação de strings)
