while True:
    s = input("Знак: ")
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print(x + y)
        elif s == '-':
            print(x - y)
        elif s == '*':
            print(x * y)
        elif s == '/':
            if y != 0:
                print(x / y)
            else:
                print("На ноль делить нельзя")
    else:
        print("Знак операции неверный")
