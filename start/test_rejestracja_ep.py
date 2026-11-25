"""Klasy równoważności (EP) – formularz rejestracji SklepTO."""
import pytest
from selenium.webdriver.common.by import By

from formularz import (oczekuj_bledu, oczekuj_sukcesu,
                       unikalny_login, zarejestruj)
from konfiguracja import SKLEPTO_URL


def test_poprawna_rejestracja(driver):
    login = unikalny_login()
    zarejestruj(driver, login=login)    # same klasy poprawne
    oczekuj_sukcesu(driver)
    driver.get(f"{SKLEPTO_URL}/admin.php")
    wiersz = driver.find_element(
        By.CSS_SELECTOR, f"#uzytkownicy tr[data-login='{login}']")
    assert wiersz.find_element(By.CLASS_NAME, "wiek").text == "30"


@pytest.mark.parametrize("login", [
    pytest.param("ab", id="za-krotki"),
    # TODO: pozostałe klasy niepoprawne loginu z tabeli EP
])
def test_login_niepoprawny(driver, login):
    zarejestruj(driver, login=login)
    oczekuj_bledu(driver, "login")


def test_login_zajety(driver):
    """Login 'jan' istnieje w danych startowych."""
    pytest.skip("TODO")


def test_unikalnosc_loginu(driver):
    """Ten sam nowy login dwa razy (użyj fixture czysta_baza)."""
    pytest.skip("TODO")


def test_email_niepoprawny(driver):
    """Sparametryzuj klasy niepoprawne e-maila."""
    pytest.skip("TODO")


def test_wiek_niepoprawny(driver):
    """Sparametryzuj klasy niepoprawne wieku."""
    pytest.skip("TODO")


def test_haslo_niepoprawne(driver):
    """Sparametryzuj klasy niepoprawne hasła (haslo2 = haslo)."""
    pytest.skip("TODO")


def test_hasla_rozne(driver):
    pytest.skip("TODO")


def test_brak_regulaminu(driver):
    pytest.skip("TODO")


def test_przegladarka_filtruje_litery_w_polu_wiek(driver):
    """Wpisz 'abc' do #wiek BEZ zmiany typu pola – jaka wartość?"""
    pytest.skip("TODO")
