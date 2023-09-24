a = 0
b = 12


def test(x, y):
    return  x // y

while a < 10000:
    a = a + 1
    print(str(a) + " / " + str(b) + " = " + str(test(a, b)))

#######################################

a = int(input("nombre : "))

print(str(a // 12) + " " + str(a % 12))
