class node:
    def __init__(self) -> None:
        # хранение
        self.symma = ''
        # хранение вероятности или частоты
        self.probability = 0.0
        self.array = [0] * 20
        self.top = 0


p = [node() for _ in range(20)]


# алгоритм Шеннона
def shannon(l, h, p):
    pack1 = 0;
    pack2 = 0;
    diff1 = 0;
    diff2 = 0
    if ((l + 1) == h or l == h or l > h):
        if (l == h or l > h):
            return
        p[h].top += 1
        p[h].array[(p[h].top)] = 0
        p[l].top += 1
        p[l].array[(p[l].top)] = 1

        return

    else:
        for i in range(l, h):
            pack1 = pack1 + p[i].probability
        pack2 = pack2 + p[h].probability
        diff1 = pack1 - pack2
        if (diff1 < 0):
            diff1 = diff1 * -1
        j = 2
        while (j != h - l + 1):
            k = h - j
            pack1 = pack2 = 0
            for i in range(l, k + 1):
                pack1 = pack1 + p[i].probability
            for i in range(h, k, -1):
                pack2 = pack2 + p[i].probability
            diff2 = pack1 - pack2
            if (diff2 < 0):
                diff2 = diff2 * -1
            if (diff2 >= diff1):
                break
            diff1 = diff2
            j += 1

        k += 1
        for i in range(l, k + 1):
            p[i].top += 1
            p[i].array[(p[i].top)] = 1

        for i in range(k + 1, h + 1):
            p[i].top += 1
            p[i].array[(p[i].top)] = 0

        # Invoke shannon function
        shannon(l, k, p)
        shannon(k + 1, h, p)


# сортировка символов на основе вероятности и частоты
def sortByProbability(n, p):
    temp = node()
    for j in range(1, n):
        for i in range(n - 1):
            if ((p[i].probability) > (p[i + 1].probability)):
                temp.probability = p[i].probability
                temp.symma = p[i].symma

                p[i].probability = p[i + 1].probability
                p[i].symma = p[i + 1].symma

                p[i + 1].probability = temp.probability
                p[i + 1].symma = temp.symma


# отображение кода
def display(n, p):
    print("\n\n\n\tSymbol       Probability         Code", end='')
    for i in range(n - 1, -1, -1):
        print("\n\t", p[i].symma, "\t\t", p[i].probability, "\t", end='')
        for j in range(p[i].top + 1):
            print(p[i].array[j], end='')


# основная функция
if __name__ == '__main__':
    total = 0
    symbol_array = {}

    # введение строки
    my_name = str(input("Enter your name:")).lower()

    # заполение вероятностей
    for i in range(0, len(my_name)):
        if my_name[i] != " ":
            if len(symbol_array) < 9:
                symbol_array[my_name[i]] = (len(my_name) - len(my_name.replace(my_name[i], ""))) / len(my_name)
                [symbol_array.update({k: v}) for k, v in symbol_array.items() if v not in symbol_array.values()]
            else:
                symbol_array[my_name[i]] = 1 - sum(symbol_array.values())
                [symbol_array.update({k: v}) for k, v in symbol_array.items() if v not in symbol_array.values()]
                break

    # ключи словаря
    for i in range(0, 10):
        print("Symbol", i + 1, " : ", end="")
        ch = str(list(symbol_array.keys())[i])
        print(ch)

        # символ в node
        p[i].symma += ch

    x = list(symbol_array.values())
    for i in range(0, 10):
        print("\nProbability of", p[i].symma, ": ", end="")
        print(x[i])

        # значение в node
        p[i].probability = x[i]
        total = total + p[i].probability

        # проверка максимальной вероятности
        if (total > 1):
            print("Invalid. Enter new values")
            total = total - p[i].probability
            i -= 1

    i += 1
    p[i].probability = 1 - total
    # Сортировка символов их вероятности или частоты
    n = 10
    sortByProbability(n, p)

    for i in range(n):
        p[i].top = -1

    # Нахождение код Шеннона
    shannon(0, n - 1, p)

    # Отображение кодов
    display(n, p)