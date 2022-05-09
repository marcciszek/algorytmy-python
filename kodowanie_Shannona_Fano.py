

def znajdz_kody_liter(slownik: dict, slownik_wynikow: dict, kod: str = ""):
    """Funkcja ta rekurencyjnie na podstawie podanego slownika (posortowanego), tworzy slowa kodowe
        z wykorzystaniem algorytmy Shannona Fano, ktore sa zapisywane w podanym slowniku_wynikow"""

    # Jesli nie mozna wiecej podzielic slownika, tworzone sa kady na podstawie "przebytej drogi"
    if len(slownik) < 2:
        for item in slownik.items():
            slownik_wynikow[item[0]] = kod

    # Dzielenie slownika na dwa mniejsze
    else:
        dl_slownika = len(slownik)
        roznica_min = float('inf')
        i_min = 0

        # Znalezienie optymalnego srodka w ktorym mozna podzielic slownik
        for i in range(1, dl_slownika):
            suma_a = 0
            suma_b = 0
            for j, value in enumerate(slownik.values()):
                if 0 <= j < i:
                    suma_a = round(suma_a + value, 16)
                elif i <= j < dl_slownika:
                    suma_b = round(suma_b + value, 16)
            if round(abs(suma_a-suma_b), 16) < roznica_min:
                roznica_min = round(abs(suma_a-suma_b), 16)
                i_min = i
                if roznica_min == 0:
                    break
        slownik_lewy = {}
        slownik_prawy = {}

        # Stworzenie dwoch slownikow oraz rekurencyjne wywolanie funkcji
        for i, item in enumerate(slownik.items()):
            if i < i_min:
                slownik_lewy[item[0]] = item[1]
            else:
                slownik_prawy[item[0]] = item[1]
        znajdz_kody_liter(slownik_lewy, slownik_wynikow, kod + '0')
        znajdz_kody_liter(slownik_prawy, slownik_wynikow, kod + '1')


def shannon_fano(slownik: dict, tekst: str = ""):
    """Funkcja ktora przyjmuje slownik, zawierajacy pary: litera i jej prawdopodobienstwo wystapienia
        oraz opcjonalnie kod do zakodowania, wynikiem jest slownik zawierajacy kody, lub zakodowany
        tekst jesli zostal podany"""
    # Sortowanie slownika
    posortowany = dict(sorted(slownik.items(), key=lambda item_val: item_val[1], reverse=True))

    # Rekurencyjne tworzenie slow kodowych
    slownik_kodowy = {}
    znajdz_kody_liter(posortowany, slownik_kodowy)

    # Zwrocenie odpowiedniego slownika lub zakodowanego tekstu
    if tekst == "":
        return dict(sorted(slownik_kodowy.items()))
    else:
        zakodowany = ""
        for char in tekst:
            zakodowany = zakodowany + slownik_kodowy[char]
        return zakodowany


slownik_1 = {'A': 0.3, 'B': 0.1, 'C': 0.1, 'D': 0.2, 'E': 0.3}
slownik_2 = {'A': 0.3, 'B': 0.2, 'C': 0.1}

print(shannon_fano(slownik_1))
print(shannon_fano(slownik_1, "BACA"))

print(shannon_fano(slownik_2))
print(shannon_fano(slownik_2, "ABC"))
