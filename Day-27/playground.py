def add(*args):
    total = 0
    for n in args:
        total += n
    return total

# print(add(1,2,3,4))


def test(*args):
    print(args)

#
# test(1, 2, 3, 5)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)