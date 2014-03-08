
def something():
    for i in range(10):
        yield i


for x in something():
    print x


def another():
    for x in range(0, 3):
        yield x
        for y in range(5, 8):
            yield y
            for z in range(9, 11):
                yield z


for x in another():
    print x
