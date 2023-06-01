"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser


@pytest.fixture(params=[(1980, 1080), (1280, 1024)])
def browser_size_desktop(request):
    size = request.param
    browser.open()
    browser.driver.set_window_size(size[0], size[1])
    yield browser
    browser.quit()


@pytest.fixture(params=[(360, 640), (390, 844)])
def browser_size_mobile(request):
    size = request.param
    browser.open()
    browser.driver.set_window_size(size[0], size[1])
    yield browser
    browser.quit()


def test_github_desktop(browser_size_desktop):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-up").click()


def test_github_mobile(browser_size_mobile):
    browser.open("https://github.com/")
    browser.element(".Button--link").click()
    browser.element(".HeaderMenu-link--sign-in").click()
