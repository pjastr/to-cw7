"""Analiza wartości brzegowych (AWB): 2- i 3-punktowa."""
import pytest

from formularz import (haslo_o_dlugosci, sprawdz_wynik,
                       unikalny_login, zarejestruj)

# (wartość, czy należy do klasy poprawnej)
WIEK_2P = []     # TODO: 4 wartości z tabeli AWB
WIEK_3P = []     # TODO: 6 wartości
LOGIN_2P = []    # TODO: długości loginu
LOGIN_3P = []    # TODO
HASLO_2P = []    # TODO: długości hasła
HASLO_3P = []    # TODO


def przypadki(dane):
    return [pytest.param(w, ok, id=str(w)) for w, ok in dane]


@pytest.mark.parametrize("wiek, poprawna", przypadki(WIEK_2P))
def test_wiek_2p(driver, wiek, poprawna):
    zarejestruj(driver, wiek=str(wiek))
    sprawdz_wynik(driver, "wiek", poprawna)


@pytest.mark.parametrize("wiek, poprawna", przypadki(WIEK_3P))
def test_wiek_3p(driver, wiek, poprawna):
    zarejestruj(driver, wiek=str(wiek))
    sprawdz_wynik(driver, "wiek", poprawna)


# TODO: test_login_dlugosc_2p / _3p – login=unikalny_login(dl)
# TODO: test_haslo_dlugosc_2p / _3p – haslo=haslo_o_dlugosci(dl)
