class Cadena06:
    __numEntero = int (0)
    __entroaCadena = str()

def __entroaCadena(__numEntero):

    for x in str(__numEntero):
        signo = "-"

        if __numEntero < 0:
            return signo + str(__numEntero * (-1))
        else:
            signo = "+"
            if __numEntero > 0:
                return signo + str(__numEntero)


__numEntero = 5

c = __entroaCadena(__numEntero)
print(c)