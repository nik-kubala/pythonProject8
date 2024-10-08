def colatz(cislo):
    while cislo > 1:
        if cislo % 2 == 0:
            cislo = cislo // 2
            print(cislo, end = ", ")
        else:
            cislo = cislo * 3 + 1
            print(cislo, end = ", ")

#colatz(10)


def delenie(n):
    deli = 2
    while n != 1:
        if n % deli == 0:
            n = n // deli
            print(deli)
        else:
            deli = deli + 1
#delenie(12)
#print("1")


def sucdel(n):
    x = 0
    for i in range(1, n + 1):
        if n % i == 0:
            x = x + i
    return x


def is_prefect(n):
    if sucdel(n) == n * 2:
        return True
    else:
        return False

for i in range(1,101):
    if is_prefect(i) == True:
        print(i)





#DOMACA ULOHA
#1.
def poc_cif(n):
    poc = 0
    while n != 0:
        poc += 1
        n = n // 10
    return poc

12 34 56
def shreder(n):
    pozicia = poc_cif(n) // 2
    if poc_cif(n) % 2 == 0:
        sucet = 0
        while n != 0:
            if poc == pozicia:
                poc += 1
                sucet = sucet + n % 10
            n = n // 10
        return sucet
    else:
        sucet = 0
        while n != 0:
            if poc == pozicia:
                poc += 1
                sucet = sucet + n % 10
            n = n // 10
        return sucet


#2.
