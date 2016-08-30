from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# cria uma instancia prototipo
stock_prototype = Stock('', 0, 0.0, None, None)

# funcao para converter um dicionario em um Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {
    'name': 'ACME',
    'shares': 100,
    'price': 123.45
}

print(dict_to_stock(a))

b = {
    'name': 'ACME',
    'shares': 100,
    'price': 123.45,
    'date': '12/17/2012'
}

print(dict_to_stock(b))


