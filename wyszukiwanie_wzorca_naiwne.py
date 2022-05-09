test = "0123456789"
text1 = "To jest przykladowy tekst z ktorego bede szukal wzorca"

def wyszukiwanie_wzorca_naiwne(wzorzec ,text):
    if len(text) < len(wzorzec):
        return -2
    zakres = len(text) - len(wzorzec)
    for i in range(0, zakres + 1):
        for j in range(0, len(wzorzec)):
            if text[i+j] != wzorzec[j]:
                break
        else:
            return i
    return -1

# funkcja zwraca indeks od ktorego zaczyna sie pierwsze wystapienie wzorca
# funkcja zwraca -1 gdy wzorca nie odnaleziono
# funckja zwraca -2 gdy wzorzec jest dluzszy od przeszukiwanego tekstu
print(wyszukiwanie_wzorca_naiwne("0123456789", test))
print(wyszukiwanie_wzorca_naiwne("56789", test))
print(wyszukiwanie_wzorca_naiwne("jest", text1))
print(wyszukiwanie_wzorca_naiwne("wzorca", text1))
print(wyszukiwanie_wzorca_naiwne("tego tam nie ma", text1))
print(text1[3:7])
print(text1[48:54])