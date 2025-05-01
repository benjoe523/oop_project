from datetime import date
from typing import List
from entities.vehicle import Jarmu
from repositories.rental_repo import KolcsonzoAdattar

class KolcsonzoSzolgaltatas:
    def __init__(self, adattar: KolcsonzoAdattar):
        self.adattar = adattar

    def jarmu_hozzaadasa(self, jarmu: Jarmu) -> None:
        self.adattar.mentes(jarmu)

    def jarmu_kolcsonzese(self, rendszam: str, datum: date, napok: int, nev: str) -> float:
        jarmu = self.adattar.keres(rendszam)
        if not jarmu:
            raise ValueError("A jármű nem található")

        kezdet = datum
        vege = datum.toordinal() + napok - 1
        for foglalas in jarmu.foglalasok:
            f_datum, f_napok = foglalas[:2]
            f_kezd = f_datum.toordinal()
            f_veg = f_kezd + f_napok - 1
            if not (vege < f_kezd or kezdet.toordinal() > f_veg):
                raise ValueError("A jármű ezen az időszakon belül már foglalt")

        jarmu.foglalasok.append((datum, napok, nev))
        self.adattar.frissites(jarmu)
        return jarmu.napi_dij * napok

    def kolcsonzes_lemondasa(self, rendszam: str, nev: str, datum: date) -> None:
        jarmu = self.adattar.keres(rendszam)
        if not jarmu:
            raise ValueError("A jármű nem található")

        foglalas_talalat = None
        for i, (f_datum, f_napok, f_nev) in enumerate(jarmu.foglalasok):
            if f_datum == datum and f_nev.strip().lower() == nev.strip().lower():
                foglalas_talalat = i
                break

        if foglalas_talalat is not None:
            del jarmu.foglalasok[foglalas_talalat]
            self.adattar.frissites(jarmu)
        else:
            raise ValueError("Nem található ilyen foglalás ezzel a névvel és dátummal.")

    def elerheto_jarmuvek(self) -> List[Jarmu]:
        return [j for j in self.adattar.osszes() if j.elerheto]
