def sortProductsCats(cats, shoes, skirts, bags):
    pCats = {}
    products = [[] for _ in range(cats.count())]
    for i in shoes:
        products[0].append({
            "id" : i.id,
            "pType" : i.productType.id,
            "name" : i.name,
            "brand" : i.brand,
            "desc" : i.desc,
            "thumbnail1" : i.thumbnail1.url,
            "thumbnail2" : i.thumbnail2.url,
            "thumbnail3" : i.thumbnail3.url,
            "rentPrice" : i.rentPrice,
            "retailPrice" : i.retailPrice

        })
    for i in skirts:
        products[1].append({
            "id" : i.id,
            "pType" : i.productType.id,
            "name" : i.name,
            "brand" : i.brand,
            "desc" : i.desc,
            "thumbnail1" : i.thumbnail1.url,
            "thumbnail2" : i.thumbnail2.url,
            "thumbnail3" : i.thumbnail3.url,
            "rentPrice" : i.rentPrice,
            "retailPrice" : i.retailPrice

        })
    for i in bags:
        products[2].append({
            "id" : i.id,
            "pType" : i.productType.id,
            "name" : i.name,
            "brand" : i.brand,
            "desc" : i.desc,
            "thumbnail1" : i.thumbnail1.url,
            "thumbnail2" : i.thumbnail2.url,
            "thumbnail3" : i.thumbnail3.url,
            "rentPrice" : i.rentPrice,
            "retailPrice" : i.retailPrice

        })
    # print(products)
    for i, c in enumerate(cats):
        
        if len(products[i]) != 0:
            catProducts = {i["id"]:i for i in products[i] if i["pType"] == c.id}
            pCats[str(c.id)] = {
                "catName" : c.typeName,
                "cp" : catProducts
            }
    return pCats





            # "qtyin" : vid.uploadDate,
            # "usSize8_0" : vid.usSize8_0,
            # "usSize8_5" : vid.usSize8_5,
            # "usSize9_0" : vid.usSize9_0,
            # "usSize9_5" : vid.usSize9_5,
            # "usSize10_0" : vid.usSize10_0,
            # "usSize10_5" : vid.usSize10_5,
            # "usSize11_0" : vid.usSize11_0,
            # "usSize11_5" : vid.usSize11_5,
            # "usSize12_0" : vid.usSize12_0