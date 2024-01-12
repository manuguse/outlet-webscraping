def getStores():
    import requests
    import json
    import html

    cont = 0
    allStores = set()
    while True:
        request = requests.post(f'https://iguatemi.com.br/ifashionoutletsc/index.php/views/ajax?_wrapper_format=drupal_ajax', data={
            'view_name':'store', 'view_display_id':'page_store_search', 'page':cont
        })
        content = request.content.decode('utf-8')
        json_content = json.loads(content)
        content = json_content[-1]['data']
        

        content = content.split('<div class=\"title\">')
        
        stores = set([html.unescape(store.split('<span>')[1].split('<')[0]).lower() for store in content[1:]])
        if len(stores) == 0:
            break
        else:
            allStores |= stores
            cont += 1
            
    return allStores