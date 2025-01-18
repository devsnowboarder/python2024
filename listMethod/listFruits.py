

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

fruits = ['apple','orange','green']
for f in fruits:
    print(f)

itr = iter(fruits)
print(next(itr))
print(next(itr))
print(next(itr))




print(is_iterable(fruits))
print(is_iterable(10))