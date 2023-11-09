lista_inteira = []
pares = []
impares = []
quantidade = int(input('Digite a quantidade de itens que deseja digitar: '))

for i in range(quantidade):
    lista_inteira.append(int(input('Digite um número: ')))
    
for i in lista_inteira:
    if i % 2 == 0:
        pares.append(i)
    elif i % 2 != 0:
        impares.append(i)
print(f'\nLista: {lista_inteira}')
print(f'Ímpares: {impares}')
print(f'Pares: {pares}')