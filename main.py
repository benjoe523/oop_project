
from datetime import date
from repositories.rental_repo import KolcsonzoAdattar
from services.rental_service import KolcsonzoSzolgaltatas
from services.ui_service import FelhasznaloiInterfesz
from entities.car import Szemelyauto
from entities.truck import Teherauto

def inicializalas():
    adattar = KolcsonzoAdattar()
    szolgaltatas = KolcsonzoSzolgaltatas(adattar)

    szolgaltatas.jarmu_hozzaadasa(Szemelyauto("ABC-123", "Toyota Corolla", 15000, 5))
    szolgaltatas.jarmu_hozzaadasa(Teherauto("DEF-456", "Ford Transit", 25000, 3500))
    szolgaltatas.jarmu_hozzaadasa(Szemelyauto("GHI-789", "Volkswagen Golf", 14000, 5))
    szolgaltatas.jarmu_hozzaadasa(Teherauto("JKL-321", "Mercedes Sprinter", 28000, 3000))
    szolgaltatas.jarmu_hozzaadasa(Szemelyauto("MNO-654", "Suzuki Swift", 12000, 4))

    szolgaltatas.jarmu_kolcsonzese("DEF-456", date(2025, 5, 2), 3, "Kiss Péter")
    szolgaltatas.jarmu_kolcsonzese("GHI-789", date(2025, 5, 5), 5, "Nagy Eszter")
    szolgaltatas.jarmu_kolcsonzese("MNO-654", date(2025, 4, 28), 7, "Tóth Ádám")

    return FelhasznaloiInterfesz(szolgaltatas)

if __name__ == "__main__":
    ui = inicializalas()
    ui.futtat()
