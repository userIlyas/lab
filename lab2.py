from math import log2
import numpy as np
from numpy import matrix
import numpy

information = {
    " ": 0.175, "о": 0.09, "е": 0.072, "а": 0.062, "и": 0.062, "н": 0.053, "т": 0.053,
    "с": 0.045, "р": 0.04, "в": 0.038, "л": 0.035, "к": 0.028, "м": 0.026, "д": 0.025,
    "п": 0.023, "у": 0.021, "я": 0.018, "ы": 0.016, "з": 0.016, "ь": 0.014, "ъ": 0.014,
    "б": 0.014, "г": 0.013, "ч": 0.012, "й": 0.01, "х": 0.009, "ж": 0.007, "ю": 0.006,
    "ш": 0.006, "ц": 0.004, "щ": 0.003, "э": 0.003, "ф": 0.002
}

mm = matrix([["     "] * 4] * 4)
M = np.array(mm)

nn = matrix([["     "] * 4] * 4)
N = np.array(mm)


def main():
    """
    3.2
    Для определения диагональных элементов необходимо воспользоваться свойством
    канальной матрицы, описывающей со стороны входа.
    Сумма элементов в каждой строке такой матрицы равна 1.
    """
    for i in range(0, 4):
        for j in range(0, 4):
            if i == j:
                M[i][j] = 0
            else:
                M[i][j] = str(input(f"Enter {i} and {j} element: "))
                M[i][j] = dict((new_k, new_val) for new_k, new_val in information.items()).get(M[i][j])
    quantity = 0
    for i in range(0, 4):
        if i == 1:
            M[0][0] = 1 - quantity
            quantity = 0
        if i == 2:
            M[1][1] = 1 - quantity
            quantity = 0
        if i == 3:
            M[2][2] = 1 - quantity
            quantity = 0
            for j in range(0, 4):
                quantity += float(M[i][j])
            M[3][3] = 1 - quantity
        for j in range(0, 4):
            quantity += float(M[i][j])
    print("Matrix 3.2 p(a): ")
    print(M)

    """
    3.3
    При построении матрицы необходимо прежде всего выбрать вероятности появления символов. 
    Выбор значений вероятностей определяется условием.
    Элементы матрицы   могут быть вычислены с помощью соотношения
    """
    for i in range(0, 4):
        for j in range(0, 4):
            if i == 0:
                N[i][j] = float(str(M[i][j]).replace("'", "")) * 0.1
            if i == 1:
                N[i][j] = float(str(M[i][j]).replace("'", "")) * 0.2
            if i == 2:
                N[i][j] = float(str(M[i][j]).replace("'", "")) * 0.3
            if i == 3:
                N[i][j] = float(str(M[i][j]).replace("'", "")) * 0.4
    print("matrix 3.3 p(a,b) \n", N)

    """
    3.4
    Найти вероятности.
    Для вычисления вероятностей необходимо воспользоваться другим замечательным свойством матрицы.
    """
    b0 = b1 = b2 = b3 = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if j == 0:
                b0 += float(str(N[i][j]).replace("'", ""))
            if j == 1:
                b1 += float(str(N[i][j]).replace("'", ""))
            if j == 2:
                b2 += float(str(N[i][j]).replace("'", ""))
            if j == 3:
                b3 += float(str(N[i][j]).replace("'", ""))
    print(f"matrix 3.4 p(a,b):\nb0={b0},\nb1={b1},\nb2={b2},\nb3={b3}")

    """
    3.5
    Канальная матрица 
    """
    for i in range(0, 4):
        for j in range(0, 4):
            if j == 0:
                N[i][j] = float(str(N[i][j]).replace("'", "")) / b0
            if j == 1:
                N[i][j] = float(str(N[i][j]).replace("'", "")) / b1
            if j == 2:
                N[i][j] = float(str(N[i][j]).replace("'", "")) / b2
            if j == 3:
                N[i][j] = float(str(N[i][j]).replace("'", "")) / b3
    print("matrix 3.5 p(a/b):\n", N)

    """
    3.6
    Найти частные условные энтропии 
    H(b/a1) and H(a/b1) 
    """
    enthropy_b_a1 = enthropy_a_b1 = 0
    i = 1
    for j in range(0, 4):
        enthropy_b_a1 += float(str(N[i][j]).replace("'", "")) * log2(float(str(N[i][j]).replace("'", "")))
    enthropy_b_a1 *= -1

    j = 1
    for i in range(0, 4):
        enthropy_a_b1 += float(str(N[i][j]).replace("'", "")) * log2(float(str(N[i][j]).replace("'", "")))
    enthropy_a_b1 *= -1
    print(f"3.6\nH(b/a1) = {enthropy_b_a1} and H(a/b1) = {enthropy_a_b1}")

    """
    3.7
    Найти  энтропии 
    H(b/a) and H(a/b) 
    """
    enthropy_b_a = enthropy_a_b = 0
    a0 = 0.1
    a1 = 0.2
    a2 = 0.3
    a3 = 0.4
    for i in range(0, 4):
        for j in range(0, 4):
            if i == 0:
                enthropy_b_a += a0 * (float(str(M[i][j]).replace("'", "")) * log2(float(str(M[i][j]).replace("'", ""))))
            elif i == 1:
                enthropy_b_a += a1 * (float(str(M[i][j]).replace("'", "")) * log2(float(str(M[i][j]).replace("'", ""))))
            elif i == 2:
                enthropy_b_a += a2 * (float(str(M[i][j]).replace("'", "")) * log2(float(str(M[i][j]).replace("'", ""))))
            elif i == 3:
                enthropy_b_a += a3 * (float(str(M[i][j]).replace("'", "")) * log2(float(str(M[i][j]).replace("'", ""))))
    enthropy_b_a *= -1
    print(f"enthropy H(b/a) = {enthropy_b_a}")

    for i in range(0, 4):
        for j in range(0, 4):
            if j == 0:
                enthropy_a_b += b0 * float(str(M[i][j]).replace("'", "")) * 0.1 * log2(float(str(M[i][j]).replace("'", "")) * 0.1)
            elif j == 1:
                enthropy_a_b += b1 * float(str(M[i][j]).replace("'", "")) * 0.1 * log2(float(str(M[i][j]).replace("'", "")) * 0.1)
            elif j == 2:
                enthropy_a_b += b2 * float(str(M[i][j]).replace("'", "")) * 0.1 * log2(float(str(M[i][j]).replace("'", "")) * 0.1)
            elif j == 3:
                enthropy_a_b += b3 * float(str(M[i][j]).replace("'", "")) * 0.1 * log2(float(str(M[i][j]).replace("'", "")) * 0.1)

    enthropy_a_b *= -1
    print(f"enthropy H(a/b) = {enthropy_a_b}")

    """
    3.7
    Найти  энтропии объединения 
    H(а) and H(и) 
    """
    h_b = h_a = 0
    h_a_b = 0
    for j in range(0, 4 ):
        if j == 0:
            h_b += b0 * log2(b0)
        if j == 1:
            h_b += b1 * log2(b1)
        if j == 2:
            h_b += b2 * log2(b2)
        if j == 3:
            h_b += b3 * log2(b3)
    h_b *= -1

    for i in range(0, 4):
        if i == 0:
            h_a += a0 * log2(a0)
        if i == 1:
            h_a += a1 * log2(a1)
        if i == 2:
            h_a += a2 * log2(a2)
        if i == 3:
            h_a += a3 * log2(a3)
    h_a *= -1

    h_a_b = h_a + enthropy_b_a

    """
    The end
    """
    print(f"I(A, B) = {-1*(h_a + h_b - h_a_b)}")
    print(f"I(A, B) = {-1*(h_a - enthropy_a_b)}")
    print(f"I(A, B) = {-1*(h_b - enthropy_b_a)}")


if __name__ == "__main__":
    main()

