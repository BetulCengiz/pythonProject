def harmonik_toplam(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonik_toplam(n-1)


def harmoniktoplamiteratif(n):
    toplam = 0
    for i in range (1, n+1):
        toplam = toplam + 1
    return  toplam

print(harmonik_toplam(4))
print(harmoniktoplamiteratif(4))
