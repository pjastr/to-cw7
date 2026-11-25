"""Shared fixtures for Selenium tests (copy into the test folder)."""
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """A new Chrome browser for each test; closed after the test."""
    drv = webdriver.Chrome()   # Selenium Manager picks chromedriver itself
    drv.implicitly_wait(0)     # we use explicit waits (WebDriverWait)
    yield drv
    drv.quit()
