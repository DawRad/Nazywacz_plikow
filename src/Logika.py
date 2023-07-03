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
