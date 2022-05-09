

class LiscLitera:
    """Obiekty beda lisciami drzewa zawierajacymi litere i jej prawdopodobienstwo wystapienia"""
    def __init__(self, litera: chr, prawdopodobienstwo: float):
        self.prawdo = prawdopodobienstwo
        self.litera = litera


class Wezel:
    """Obiekty beda wezlami, w ktorych bedzie prawdopodobienstwo laczne oraz wskazanie do kolejnych obiektow"""
    def __init__(self, prawy_element, lewy_element):
        self.prawdo = round(lewy_element.prawdo + prawy_element.prawdo, 16)
        self.lewy = lewy_element
        self.prawy = prawy_element


def znajdz_kod_liscia(element, slownik_wynikow: dict, kod=""):
    """Funkcja ta tworzy kody na podstawie drzewa, nalezy podac korzen drzewa jako pierwszy parametr
        oraz pusty slownik do ktorego bedzie wpisany wynik jako drugi"""
    if type(element) == Wezel:
        znajdz_kod_liscia(element.lewy, slownik_wynikow, kod + '0')
        znajdz_kod_liscia(element.prawy, slownik_wynikow, kod + '1')
    elif type(element) == LiscLitera:
        slownik_wynikow[element.litera] = kod


def huffman(slownik: dict, tekst: str = ""):
    """Funkcja ktora przyjmuje slownik, zawierajacy pary: litera i jej prawdopodobiensto wystapienia
        oraz opcjonalnie tekst do zakodowania, wynikiem jest slownik zawierajacy kody, lub zakodowany
        tekst jesli zostal podany"""

    # Tworzenie lisci z podanego slownika
    zbior_drzew = []
    for item in slownik.items():
        zbior_drzew.append(LiscLitera(item[0], item[1]))

    # Tworzenie drzewa binarnego
    while len(zbior_drzew) > 1:
        zbior_drzew.sort(key=lambda x: x.prawdo, reverse=True)
        nowy_wezel = Wezel(zbior_drzew.pop(), zbior_drzew.pop())
        zbior_drzew.append(nowy_wezel)

    # Tworzenie slownika na podstawie drzewa binarnego
    slownik_kodowy = {}
    znajdz_kod_liscia(zbior_drzew[0], slownik_kodowy)

    # Zwrocenie odpowiednia slownika lub zakodowanego tekstu
    if tekst == "":
        return dict(sorted(slownik_kodowy.items()))
    else:
        zakodowany = ""
        for char in tekst:
            zakodowany = zakodowany + slownik_kodowy[char]
        return zakodowany


slownik_1 = {'A': 0.3, 'B': 0.1, 'C': 0.2, 'D': 0.1, 'E': 0.2, 'F': 0.1}
print(huffman(slownik_1))
print(huffman(slownik_1, "BACA"))

slownik_2 = {'A': 0.35, 'B': 0.17, 'C': 0.17, 'D': 0.16, 'E': 0.15}
print(huffman(slownik_2))
print(huffman(slownik_2, "BACA"))

slownik_3 = {'A': 0.3, 'B': 0.3, 'C': 0.2, 'D': 0.1, 'E': 0.1}
print(huffman(slownik_3))
print(huffman(slownik_3, "BACA"))
