from typing import List, Optional
from entities.vehicle import Jarmu

class KolcsonzoAdattar:
    def __init__(self):
        self._jarmuvek = []

    def mentes(self, jarmu: Jarmu) -> None:
        self._jarmuvek.append(jarmu)

    def keres(self, rendszam: str) -> Optional[Jarmu]:
        for j in self._jarmuvek:
            if j.rendszam == rendszam:
                return j
        return None

    def frissites(self, jarmu: Jarmu) -> None:
        for i, j in enumerate(self._jarmuvek):
            if j.rendszam == jarmu.rendszam:
                self._jarmuvek[i] = jarmu
                break

    def osszes(self) -> List[Jarmu]:
        return self._jarmuvek.copy()
