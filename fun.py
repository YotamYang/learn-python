def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


def add_end(L=[]):
    L.append('END')
    return L

print add_end()
print add_end()
print add_end()

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1, 2, 3)
print calc(1, 5, 7, 9)