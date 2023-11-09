lista = []
elementos_repetidos = []

while True:
    lista.append(input('Digite qualquer coisa:  '))
    continuar = str(input('Deseja continuar[S/N]? ')).upper().strip()
    if continuar[0] == 'S':
                continue
    elif continuar[0] == 'N':
        break
print(f'\nLista: {lista}')
for elemento in lista:
    print(f'O elemento {elemento} aparece {lista.count(elemento)} vez(es) na lista.')