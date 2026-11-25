"""Fixture: przeglądarka i stan bazy danych SklepTO."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from konfiguracja import SKLEPTO_URL

# czytelne komunikaty asercji także w module pomocniczym
pytest.register_assert_rewrite("formularz")


@pytest.fixture(scope="session")
def driver():
    """Jedna przeglądarka na całą sesję testów (szybciej)."""
    drv = webdriver.Chrome()
    drv.implicitly_wait(0)
    yield drv
    drv.quit()


# TODO (krok B3): funkcja resetuj_baze(driver) oraz fixture:
#   baza_poczatkowa (scope="session", autouse=True),
#   czysta_baza (scope="function"),
#   bez_ciasteczek (autouse=True) – driver.delete_all_cookies()
