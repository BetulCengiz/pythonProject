"""
def tekrar_kaldir(x):
    return list(set(x))

# set kümeleme demektir kümelersek sadece her elemandan bir tanesini almı oluyoruz. ükmenin kuralı budur .

liste = [1, 2, 3, 4, 3, 2, 1]
print(liste)
print(tekrar_kaldir(liste))
"""
def tekrar_sil(x):
    y = []
    for eleman in x:
        if eleman not in y :
            y.append(eleman)
    return y


liste = [1, 2, 3, 4, 3, 2, 1]
print(tekrar_sil(liste))