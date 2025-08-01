def cakes(recipe, available):
    keys = recipe.keys()
    qty = []
    for key in keys:
        tmp = available.get(key, 0)
        qty.append(int(tmp / recipe[key]))
    qty.sort()
    return qty[0]
