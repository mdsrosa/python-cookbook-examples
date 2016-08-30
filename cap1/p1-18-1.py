from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


records = [
    ('AAPL', 6, 612.78,),
    ('IBM', 5, 205.55,)
]

print('records: ', records)
print('computed costs: ')
print(compute_cost(records))
