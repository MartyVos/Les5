def convert(c):
    f = c * 1.8 + 32
    return f


def table():
    print('  {}      {}'.format("F", "C"))
    for c in range(-30, 50, 10):
        f = convert(c)
        print('{:5}  {:6}'.format(f, float(c)))


table()
