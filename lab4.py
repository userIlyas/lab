information = {
    '0': '0001', '1': '0010', '2': '0011', '3': '0100', '4': '0101',
    '5': '0110', '6': '0111', '7': '1000', '8': '1001', '9': '1010'
}


def start_matrix(message: str, chet: int):
    message = message.replace(".", "")
    razn = 36 - len(message)
    message = message + razn * "0"

    M = [["0000"] * 7 for i in range(7)]
    k = 0

    for i in range(0, 6):
        for j in range(0, 6):
            M[i][j] = information[str(message[k])]
            k += 1

    y = []
    z = []
    for i in range(len(M)):
        stroki = 0
        for j in range(len(M[0])):
            one = str(M[j][i]).split()
            stroki += sum(map(int, one))  # вывод суммы отдельной строки
        stroki = stroki % chet
        y.append(stroki)  # с занесением в одномерный массив

    for i in range(len(M[0])):
        stowbtsy = 0
        for j in range(len(M)):
            one = str(M[j][i]).split()
            stowbtsy += sum(map(int, one))  # вывод суммы отдельного столбца
        stowbtsy = stowbtsy % chet
        z.append(stowbtsy)  # с занесением в одномерный массив

    for j in range(0, 7):
        M[6][j] = "..." + str(z[j])

    for i in range(0, 7):
        M[i][6] = "..." + str(y[i])

    for i in M:
        print(' '.join(list(map(str, i))))


start_matrix(input("Enter your date: "), int(input("Enter your chet-number: ")))

