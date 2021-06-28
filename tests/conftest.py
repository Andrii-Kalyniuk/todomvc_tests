import pytest
from selene.support.shared import browser

from config import settings


def _set_custom_driver(settings):
    from selenium import webdriver

    options = None
    if settings.browser_name == 'chrome':
        options = webdriver.ChromeOptions()
    elif settings.browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
    options.headless = settings.headless

    if settings.remote_url:
        options.set_capability('enableVNC', settings.remote_enable_vnc)
        options.set_capability('screenResolution',
                               settings.remote_screen_resolution)
        driver = webdriver.Remote(settings.remote_url,
                                  options=options)
    else:
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.firefox import GeckoDriverManager
        driver = {
            'chrome': lambda: webdriver.Chrome(
                executable_path=ChromeDriverManager().install(),
                options=options
            ),
            'firefox': lambda: webdriver.Firefox(
                executable_path=GeckoDriverManager().install(),
                options=options
            )
        }[settings.browser_name]()

        if settings.browser_window_maximize:
            driver.maximize_window()
        else:
            driver.set_window_size(
                width=settings.browser_window_width,
                height=settings.browser_window_height)

    return driver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = settings.browser_name
    if custom_driver := _set_custom_driver(settings):
        browser.config.driver = custom_driver

    yield

    if settings.browser_quit_after_each_test:
        browser.quit()
    else:
        browser.clear_local_storage()
