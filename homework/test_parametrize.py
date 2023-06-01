"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser


@pytest.fixture(params=[(1980, 1080), (1280, 1024), (360, 640), (390, 844)])
def browser_size(request):
    size = request.param
    browser.open()
    browser.driver.set_window_size(size[0], size[1])
    yield browser
    browser.quit()


@pytest.mark.parametrize('browser_size', [(1980, 1080), (1280, 1024)], indirect=True)
def test_github_desktop(browser_size):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').click()


@pytest.mark.parametrize('browser_size', [(360, 640)], indirect=True)
def test_github_mobile(browser_size):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
