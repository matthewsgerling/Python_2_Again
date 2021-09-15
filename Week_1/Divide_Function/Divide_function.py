def dividefunction(func):
    def inner1(var1, var2):
        if var2 == 0:
            print('You cant divide by zero')
            quit(1)
        else:
            print('Doubling', var1, 'and tripling', var2)
            print(func(var1, var2))

    return inner1


@dividefunction
def divide(var1, var2):
    var1 = var1 * 2
    var2 = var2 * 3
    return var1 / var2


divide(12, 2)
