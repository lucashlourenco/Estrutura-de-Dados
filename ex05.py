lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))
lista_completa = lista1 + lista2
lista_completa.sort

print(f'\nPrimeira Lista: {lista1}')
print(f'Segunda Lista: {lista2}')
print(lista_completa)