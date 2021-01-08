def Armstrong(ust_limit):
    for i in range(1, ust_limit):
        toplam = 0
        sayi = i
        while sayi > 0:
            basamak = sayi % 10
            toplam = toplam+(basamak*basamak*basamak)
            sayi = sayi - basamak
            sayi = sayi / 10
        if i == toplam:
            print(i)
Armstrong(1000)




