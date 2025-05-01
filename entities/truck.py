from .vehicle import Jarmu

class Teherauto(Jarmu):
    def __init__(self, rendszam: str, tipus: str, napi_dij: float, teherbiras: float):
        super().__init__(rendszam, tipus, napi_dij)
        self.teherbiras = teherbiras

    def jarmu_adatok(self) -> str:
        return (f"{self.rendszam} - {self.tipus} "
                f"(Teherautó, {self.teherbiras} kg, {self.napi_dij} Ft/nap)")
