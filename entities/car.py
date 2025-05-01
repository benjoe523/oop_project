from .vehicle import Jarmu

class Szemelyauto(Jarmu):
    def __init__(self, rendszam: str, tipus: str, napi_dij: float, ulesek_szama: int):
        super().__init__(rendszam, tipus, napi_dij)
        self.ulesek_szama = ulesek_szama

    def jarmu_adatok(self) -> str:
        return (f"{self.rendszam} - {self.tipus} "
                f"(Személyautó, {self.ulesek_szama} ülés, {self.napi_dij} Ft/nap)")
