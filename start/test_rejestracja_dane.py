"""Testy sterowane danymi z plików CSV i JSON (katalog dane/)."""
import csv
from pathlib import Path

import pytest

from formularz import sprawdz_wynik, zarejestruj

DANE = Path(__file__).parent / "dane"


def wczytaj_csv(nazwa):
    """Wiersze CSV (separator ;) jako pytest.param z id."""
    with open(DANE / nazwa, encoding="utf-8-sig", newline="") as f:
        wiersze = list(csv.DictReader(f, delimiter=";"))
    return [pytest.param(w["wartosc"], w["wynik"] == "OK",
                         id=w["id"]) for w in wiersze]


@pytest.mark.parametrize("wiek, poprawna", wczytaj_csv("wiek.csv"))
def test_wiek_z_csv(driver, wiek, poprawna):
    zarejestruj(driver, wiek=wiek)
    sprawdz_wynik(driver, "wiek", poprawna)


# TODO: test_login_z_csv – dane/login.csv
# TODO (*): wczytaj_json + test_email_z_json – dane/email.json
