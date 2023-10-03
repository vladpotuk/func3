def draw_square(length, symbol, filled):
    if filled:
        for i in range(length):
            print(symbol * length)
    else:
        print(symbol * length)
        for i in range(length - 2):
            print(symbol +" " * (length - 2) + symbol)
        if length > 1:
            print(symbol * length)
print("Заповнений квадрат: ")
draw_square(5, "*", True)

print("Порожній квадрат: ")
draw_square(4, "#", False)




