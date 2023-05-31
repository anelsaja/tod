def faktorialgenap(jumlah, awal):
    if jumlah == 0:
        return 1
    else:
        return faktorialgenap(jumlah-1, awal + 2) * (awal + 2)

print(faktorialgenap(10,0))


def binary_to_dex(biner, pangkat = 0):
    if biner == "0":
        return 0
    elif biner == "1":
        return pow(2, pangkat)
    else:
        digitterakhir = int(biner[-1])
        if digitterakhir == 0:
            return binary_to_dex(biner[:-1], pangkat + 1)
        else:
            return binary_to_dex(biner[:-1], pangkat + 1) + pow(digitterakhir*2, pangkat)

def bagibiner(biner):
    pecahan = biner.split(".")
    for i in range(len(pecahan)):
        pecahan[i] = binary_to_dex(pecahan[i])
    return f"{pecahan[0]}.{pecahan[1]}.{pecahan[2]}.{pecahan[3]}"

print(bagibiner("11000000.10101000.00000001.00000010"))

def cekprima(n, divisor = 0, result = True):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif divisor == 1:
        return result
    else:
        if divisor == 0:
            divisor = n - 1
        if (n%divisor == 0):
            result = result and False
        else:
            result = result and True
        return cekprima(n, divisor - 1, result)

def cariangka(n):
    jumlah = 0
    jumlahprimaketemu = 0
    iterate = 1
    while jumlahprimaketemu < n:
        if (cekprima(iterate)):
            jumlahprimaketemu += 1
            jumlah += iterate
        iterate += 1
    return jumlah

print(cariangka(10))
