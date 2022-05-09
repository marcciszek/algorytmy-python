import sys


def wyszukiwanie_wzorca_bm(wzorzec: str, tekst: str) -> int:

    # Sprawdzenie czy tekst nie jest krotszy od wzorca
    if len(tekst) < len(wzorzec):
        raise ValueError("Tekst krotszy od poszukiwanego wzorca")

    # Stworzenie slownika, ktory wskazuje na ostatnie wystapienie danej litery ze wzorca
    ostatnie_wystapienie = {}
    for char_pozycja in range(len(wzorzec)):
        ostatnie_wystapienie[wzorzec[char_pozycja]] = char_pozycja

    licznik_wystapien = 0

    # Przeszukiwanie tekstu z wykorzystaniem algorytmu Boyer–Moore
    i = len(wzorzec) - 1
    while i < len(tekst):
        for j in range(len(wzorzec) - 1, -1, -1):
            if wzorzec[j] == tekst[i]:
                if j == 0:
                    licznik_wystapien += 1
                    i += len(wzorzec)
                else:
                    i -= 1
            else:
                i += len(wzorzec) - min(j, 1 + ostatnie_wystapienie.get(tekst[i], -1))
                break
    return licznik_wystapien


def zliczenie_wystapien_pliki(nazwa_pliku_fraza: str, nazwa_pliku_poszukiwanie: str) -> None:

    # Proba odczytania poszukiwanego wzorca, w razie niepowodzenia przerwanie i odpowiedni komunikat
    try:
        with open(nazwa_pliku_fraza, 'r', encoding='utf-8') as f_fraza:
            fraza = f_fraza.readline()
    except FileNotFoundError:
        print("*"*100)
        print("Blad!")
        print(f'Nie znaleziono pliku "{nazwa_pliku_fraza}"')
        print(f'Upewnij się, że znajduje sie on w tej samej lokalizacji co "{__name__.strip("_") + ".py"}"')
        print("*"*100)
        print()
        input("Nacisnij Enter, aby kontynuować...")

    # Proba odczytania tekstu do przeszukania, w razie niepowodzenia przerwanie i odpowiedni komunikat
    tekst_przygotowany = ""
    try:
        with open(nazwa_pliku_poszukiwanie, 'r', encoding='utf-8') as f_tekst:
            tekst_wczytany = f_tekst.readlines()
    except FileNotFoundError:
        print("*" * 100)
        print("Blad!")
        print(f'Nie znaleziono pliku "{nazwa_pliku_poszukiwanie}"')
        print(f'Upewnij się, że znajduje sie on w tej samej lokalizacji co "{__name__.strip("_") + ".py"}"')
        print("*" * 100)
        print()
        input("Nacisnij Enter, aby kontynuować...")
    else:

        for linia in tekst_wczytany:
            tekst_przygotowany += linia.strip('\n')

    # Proba przeszukania tekstu w poszukiwaniu ilosci wystapien danego wzorca
    try:
        n = wyszukiwanie_wzorca_bm(fraza, tekst_przygotowany)
    except ValueError:
        print("*" * 100)
        print("Blad!")
        print("Nie można przeprowadzić poszukiwania")
        print(f'Dlugość wzorca jest większa od długości podanego tekstu')
        print("*" * 100)
        print()
        input("Nacisnij Enter, aby kontynuować...")
    else:
        print("*"*100)
        print("Przeszukiwanie zakonczone!")
        print(f'Fraza z pliku "{nazwa_pliku_fraza}"')
        print("-" * len(fraza))
        print(fraza)
        print("-" * len(fraza))
        if n == 0:
            print(f'Nie zostala odnaleziona w pliku "{nazwa_pliku_poszukiwanie}"')
        elif n == 1:
            print(f'Znajduje sie w pliku "{nazwa_pliku_poszukiwanie}" {n} raz')
        else:
            print(f'Znajduje sie w pliku "{nazwa_pliku_poszukiwanie}" {n} razy')
        print("*"*100)
        print()
        input("Nacisnij Enter, aby kontynuować...")


def main():
    arg = False
    plik_fraza = "fraza.txt"
    plik_tekst = "tekst.txt"
    if len(sys.argv) > 2:
        plik_fraza = sys.argv[1]
        plik_tekst = sys.argv[2]
        arg = True

    while True:
        print()
        print("-" * 100)
        print("Zliczanie wystąpień danej frazy w tekście")
        print()
        print("Jeśli jesteś gotowy wpisz SZUKAJ i naciśnij Enter")
        print()
        print("Jeśli potrzebujesz pomocy wpisz HELP i naciśnij Enter")
        print("Jeśli chcesz zakończyć wpisz EXIT i naciśnij Enter")
        print("-" * 100)
        wybor = ""
        try:
            wybor = input("--> ")
        except KeyboardInterrupt:
            exit(0)
        except EOFError:
            exit(0)
        if wybor.lower() == "help":
            print("Napisane przez: Marcin Ciszek, 2021 rok")
            print("Program korzysta z kodowania utf-8")
            print()
            print("Dane należy umieścić w dwóch plikach znajdujących się obok tego programu")
            print('     -szukaną frazę należy umieścić w pliku "fraza.txt"')
            print('     -tekst do przeszukania należy umieścić w pliku "tekst.txt"')
            print()
            print("lub przekazać ścieżki bezwględne jako parametry")
            print("     -pierwsza ma prowadzić do pliku txt zawierającego poszukiwaną frazę")
            print("     -drugi ma prowadzić do pliku txt zawierającego przeszukiwany tekst")
            print()
            print("lub jako parametry przekazac inne nazwy plikow")
            print("znajdujące się w tej samej lokalizacji co program")
            print()
            input("Nacisnij Enter, aby kontynuować...")
        elif wybor.lower() == "szukaj":
            if arg:
                print("Podano nastepujace parametry:")
                print(f'Wzorzec: {plik_fraza}')
                print(f'tekst: {plik_tekst}')
                potwierdzenie = ""
                while potwierdzenie != "t" and potwierdzenie != "n":
                    potwierdzenie = input("Czy na pewno chcesz kontynowac? [t/n]").lower()
                    if potwierdzenie == "t":
                        zliczenie_wystapien_pliki(plik_fraza, plik_tekst)
            else:
                zliczenie_wystapien_pliki(plik_fraza, plik_tekst)
        elif wybor.lower() == "exit":
            print("Do zobaczenia!")
            input("Nacisnij Enter, aby kontynuować...")
            exit(0)


main()
