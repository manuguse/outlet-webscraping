def getStores():
    import requests
    import html

    cont = 1
    allStores = set()
    while True:
        request = requests.get(f'https://outletportobelo.com.br/lojas/?_paged={str(cont)}')
        content = request.content.decode('utf-8')

        content = content.split('card-loja__nome')
        
        stores = set([html.unescape(store[2:].split('<')[0]).lower() for store in content if not store.startswith('<html')])
        if len(stores) == 0:
            break
        else:
            allStores |= stores
            cont += 1
            
    return allStores