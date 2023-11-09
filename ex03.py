numeros = []

while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    numeros.append(numero)
print(f'\nMaior número: {max(numeros)}')
print(f'Menor número: {min(numeros)}')