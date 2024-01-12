import lojas_ifashion, lojas_portobelo

lojasIFashion = lojas_ifashion.getStores()
lojasPortobelo = lojas_portobelo.getStores()

print('TEM NAS DUAS:\n')
for loja in (lojasIFashion & lojasPortobelo):
    print(loja)
    
print('-'*60)
    
print('\n\nSÓ NO IFASHION:\n')
for loja in (lojasIFashion - lojasPortobelo):
    print(loja)
print()
    
print('-'*60)

print('\n\nSÓ NO PORTOBELO:\n')
for loja in (lojasPortobelo - lojasIFashion):
    print(loja)
print()
