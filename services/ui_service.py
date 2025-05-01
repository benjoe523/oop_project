from datetime import date
from entities.car import Szemelyauto
from entities.truck import Teherauto
from services.rental_service import KolcsonzoSzolgaltatas

class FelhasznaloiInterfesz:

    def __init__(self, szolgaltatas: KolcsonzoSzolgaltatas):
        self.szolgaltatas = szolgaltatas

    def menu(self):
        print("\n=== Autókölcsönző ===")
        print("1. Új jármű")
        print("2. Kölcsönzés")
        print("3. Lemondás")
        print("4. Foglalások")
        print("5. Járműlista")
        print("0. Kilépés")

    def uj_jarmu(self):
        print("\nÚj jármű hozzáadása:")
        tipus = input("Típus (1-személyautó, 2-teherautó): ")

        try:
            rendszam = input("Rendszám: ").upper()
            tipus_nev = input("Jármű típusa: ")
            napi_dij = float(input("Napi díj (Ft): "))

            if tipus == "1":
                ulesek = int(input("Ülések száma: "))
                jarmu = Szemelyauto(rendszam, tipus_nev, napi_dij, ulesek)
            elif tipus == "2":
                teherbiras = float(input("Teherbírás (kg): "))
                jarmu = Teherauto(rendszam, tipus_nev, napi_dij, teherbiras)
            else:
                print("Érvénytelen típus.")
                return

            self.szolgaltatas.jarmu_hozzaadasa(jarmu)
            print("Jármű hozzáadva.")
        except Exception as e:
            print("Hiba:", e)

    def kolcsonzes(self):
        rendszam = input("Rendszám: ").upper()
        try:
            datum_str = input("Kölcsönzés kezdete (ÉÉÉÉ-HH-NN): ")
            napok = int(input("Hány napra szeretné kölcsönözni?: "))
            nev = input("Bérlő neve: ")
            datum = date.fromisoformat(datum_str)
            ar = self.szolgaltatas.jarmu_kolcsonzese(rendszam, datum, napok, nev)
            print(f"Sikeres kölcsönzés {napok} napra. Ár: {ar} Ft")
        except Exception as e:
            print("Hiba:", e)

    def lemondas(self):
        rendszam = input("Rendszám: ").upper()
        try:
            nev = input("Bérlő neve: ")
            datum_str = input("Foglalás dátuma (ÉÉÉÉ-HH-NN): ")
            datum = date.fromisoformat(datum_str)
            self.szolgaltatas.kolcsonzes_lemondasa(rendszam, nev, datum)
            print("Kölcsönzés törölve.")
        except Exception as e:
            print("Hiba:", e)

    def foglalasok_listazasa(self):
        print("Foglalt járművek:")
        for j in self.szolgaltatas.adattar.osszes():
            if j.foglalasok:
                print(f"\n{j}")
                for f in j.foglalasok:
                    d, n, nev = f
                    print(f"  - {d.isoformat()} - {n} nap - Bérlő: {nev}")

    def jarmu_lista(self):
        print("\nÖsszes jármű:")
        for j in self.szolgaltatas.adattar.osszes():
            print(j)

    def futtat(self):
        while True:
            self.menu()
            valasztas = input("Választás: ")
            if valasztas == "1":
                self.uj_jarmu()
            elif valasztas == "2":
                self.kolcsonzes()
            elif valasztas == "3":
                self.lemondas()
            elif valasztas == "4":
                self.foglalasok_listazasa()
            elif valasztas == "5":
                self.jarmu_lista()
            elif valasztas == "0":
                print("Kilépés...")
                break
            else:
                print("Érvénytelen választás.")
