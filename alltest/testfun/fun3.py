def jc(i):
    if i == 1:
        return 1
    else:
        res = i * jc(i - 1)
    return res


def fbnq(i):
    if i == 1:
        return 1
    elif i == 2:
        return 1
    else:
        return fbnq(i - 1) + fbnq(i - 2)


for i in range(1,7):
    print(fbnq(i))
