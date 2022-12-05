from math import log2

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

information = {
    " ": 0.175, "о": 0.09, "е": 0.072, "а": 0.062, "и": 0.062, "н": 0.053, "т": 0.053,
    "с": 0.045, "р": 0.04, "в": 0.038, "л": 0.035, "к": 0.028, "м": 0.026, "д": 0.025,
    "п": 0.023, "у": 0.021, "я": 0.018, "ы": 0.016, "з": 0.016, "ь": 0.014, "ъ": 0.014,
    "б": 0.014, "г": 0.013, "ч": 0.012, "й": 0.01, "х": 0.009, "ж": 0.007, "ю": 0.006,
    "ш": 0.006, "ц": 0.004, "щ": 0.003, "э": 0.003, "ф": 0.002
}

number_info = log2(10)
symbol_info = log2(32)


def main():
    message = str(input("Enter your message: ").lower())
    number_quantity = symbol_quantity = 0
    new_message = ""
    for symbol in message:
        if symbol in numbers:
            number_quantity += 1
        else:
            symbol_quantity += 1

    s_volume = symbol_info * symbol_quantity
    print(s_volume)
    n_volume = number_info * number_quantity

    entropy1 = (s_volume + n_volume) / len(message)
    print(f"Entropy is in first time is {entropy1} bit/symbol")

    for symbol in message:
        if symbol not in numbers:
            new_message = new_message + symbol
    print("symbol        p          -1 * p * log2(p)")
    for symbol in new_message:
        p = dict((new_k, new_val) for new_k, new_val in information.items()).get(symbol)
        print(f"{symbol}            {p}      {-1*p*log2(p)}")

    symbol_entropy = 0
    for symbol in message:
        if symbol not in numbers:
            p = dict((new_k, new_val) for new_k, new_val in information.items()).get(symbol)
            symbol_entropy += -1 * p * log2(p)

    s_volume = len(new_message) * symbol_entropy
    print(s_volume)
    entropy2 = (s_volume + n_volume) / len(message)

    print(f"Symbol entropy is {symbol_quantity} bit/symbol\nEntropy2 is {entropy2} bit/symbol")

    h2 = 3.52
    h3 = 3.01

    i2 = h2 * symbol_quantity + n_volume
    print(i2)
    i3 = h3 * symbol_quantity + n_volume
    print(i3)

    entropy_2 = i2 / len(message)
    print(f"Entropy with 2 symbols is {entropy_2} bit/symbol")

    entropy_3 = i3 / len(message)
    print(f"Entropy with 3 symbols is {entropy_3} bit/symbol")


if __name__ == "__main__":
    main()
