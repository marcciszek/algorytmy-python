
def wyszukiwanie_wzorca_KR(wzorzec, tekst):
    liczba_pierwsza = 19
    rozmiar_alfabetu = 5
    alfabet = {}
    zakres = len(tekst) - len(wzorzec) + 1
    for i in range(rozmiar_alfabetu):
        alfabet[chr(ord('a') + i)] = i
    wzorzec_hash = hashowanie(wzorzec, alfabet, liczba_pierwsza)
    porownanie_hash = hashowanie(tekst[:len(wzorzec)], alfabet, liczba_pierwsza)
    for i in range(zakres):
        if wzorzec_hash == porownanie_hash:
            if tekst[i:i+len(wzorzec)] == wzorzec:
                return i
        porownanie_hash = ((porownanie_hash - alfabet[tekst[i]] * rozmiar_alfabetu ** (
                    len(wzorzec) - 1)) * rozmiar_alfabetu + alfabet[tekst[i + len(wzorzec)]]) % 19
    else:
        return -1

def hashowanie(tekst, alfabet, liczba_pierwsza):
    suma = 0
    potega = len(tekst) - 1
    for i in range (len(tekst)):
        suma += alfabet[tekst[i]]*len(alfabet)**potega
        potega -= 1
    return suma % liczba_pierwsza


print("wynik: ", wyszukiwanie_wzorca_KR("a", "aedbaca"))
print("wynik: ", wyszukiwanie_wzorca_KR("ca", "aedbaca"))
print("wynik: ", wyszukiwanie_wzorca_KR("aedbaca", "aedbaca"))
print("wynik: ", wyszukiwanie_wzorca_KR("baca", "aedbaca"))
