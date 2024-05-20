# Ex 1038
X, Y = map(float, input().split())

if X == 1:
    print("Total: R$ {:.2f}".format(4.00 * Y))
elif X == 2:
    print("Total: R$ {:.2f}".format(4.50 * Y))
elif X == 3:
    print("Total: R$ {:.2f}".format(5.00 * Y))
elif X == 4:
    print("Total: R$ {:.2f}".format(2.00 * Y))
elif X == 5:
    print("Total: R$ {:.2f}".format(1.50 * Y))
