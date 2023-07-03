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
    
    def zmienNazwePliku(self, stara_nazwa: str, nowa_nazwa: str, sciezka:str = '', rozszerzenie: str = ''):
        spr_rozszerz = nowa_nazwa.split('.')

        stara_nazwa = sciezka + stara_nazwa
        if rozszerzenie == '' and len(spr_rozszerz) == 1:
            stare_rozszerz = stara_nazwa.split('.')

            if len(stare_rozszerz) == 1:
                #TODO:
                #   trzeba jakoś zareagować, gdyby stara_nazwa też nie miała rozszerzenia
                pass
            
            nowa_nazwa = sciezka + nowa_nazwa + '.' + stare_rozszerz[len(stare_rozszerz) - 1]
        elif rozszerzenie != '' and len(spr_rozszerz) == 1:
            nowa_nazwa = sciezka + nowa_nazwa + '.' + rozszerzenie
        elif len(spr_rozszerz) > 1:
            nowa_nazwa = sciezka + nowa_nazwa

        os.rename(stara_nazwa, nowa_nazwa)      
