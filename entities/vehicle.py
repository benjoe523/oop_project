from abc import ABC, abstractmethod

class Jarmu(ABC):
    def __init__(self, rendszam: str, tipus: str, napi_dij: float):
        self.rendszam = rendszam
        self.tipus = tipus
        self.napi_dij = napi_dij
        self.foglalasok = []  # (datum, napok)
        self.foglalasok = []  # (datum, napok)

    @abstractmethod
    def jarmu_adatok(self) -> str:
        pass

    def __str__(self):
        return self.jarmu_adatok()

    @property
    def elerheto(self) -> bool:
        # Döntés dinamikusan, hogy a jármű szabad-e a mai napon
        from datetime import date
        today = date.today().toordinal()
        for foglalas in self.foglalasok:
            foglalt_datum, napok = foglalas[:2]
            start = foglalt_datum.toordinal()
            end = start + napok - 1
            if start <= today <= end:
                return False
        return True
