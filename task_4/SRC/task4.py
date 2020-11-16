def compare_two_string(x, y):
    if "*" in x:
        return("Неверный формат данных")
    tern = y.split("*")
    p = 0
    for i in tern:
        if i == "":
            continue
        else:
            try:
                z = x.index(i, p)
                p = z + len(i)
            except ValueError:
                return("KO")
    return("OK")

if __name__ == "__main__":
    x = input("Введите первую строку: ")
    y = input("Введите вторую строку: ")
    print(compare_two_string(x, y))

