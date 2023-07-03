import os

# < - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \
# < - - - - - Klasa Zarzadca - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
# < - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - /

class Zarzadca:
    def __init__(self) -> None:
        pass

    def pobierzNazwyPlikowZFolderu(self, sciezka: str):
        """ Metoda, która pobiera nazwy wszystkich plików z podanego folderu.

        Parametry
        ----------
        sciezka : str
            Ścieżka do wybranego folderu

        Zwraca
        ----------
        list() : Listę nazw plików.
        """

        res = os.listdir(sciezka)
        return res
    
    def zmienNazwePliku(self, stara_nazwa: str, nowa_nazwa: str, sciezka:str = ''):
        stara_nazwa = sciezka + stara_nazwa
        nowa_nazwa = sciezka + nowa_nazwa
        os.rename(stara_nazwa, nowa_nazwa)      
