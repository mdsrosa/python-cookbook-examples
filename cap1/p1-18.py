from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

print('sub = ', Subscriber)
print('sub.addr = ', sub.addr)
print('sub.joined = ', sub.joined)
