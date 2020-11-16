def itoBase(nb, base):
    rit1 = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    rit2 = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    dirt = "0123456789abcdef"
    for i in range(len(base)):
        if base[i] != dirt[i]:
            return("usage")
    if base[-1].isdigit():
        isc = int(base[-1]) + 1
    else:
        isc = rit2[base[-1].lower()] + 1

    zm = True
    massiv = []
    otvet = nb
    while zm:
        otvet, ostatok = otvet//isc, otvet%isc
        if ostatok > 10:
            massiv.append(rit1[ostatok])
        else:
            massiv.append(ostatok)
        if otvet < isc:
            if otvet > 10:
                massiv.append(rit1[otvet])
            else:
                massiv.append(otvet)
            zm = False
    return "".join([str(i) for i in massiv[::-1]])

if __name__ == "__main__":
    try:
        x = int(input("Введите число: "))
        y = input("Введите систему исчесления: ")
        print(itoBase(x, y))
    except ValueError:
        print("usage")



