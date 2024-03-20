import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from e2ePytestSeleniumFlow.testdata.TestData import TestData
from e2ePytestSeleniumFlow.utilities.LoggerClass import LoggerClass

browser_driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",help="my option: chrome or edge",
    )



@pytest.fixture(scope="class")
def setup(request):

    global browser_driver
    log = LoggerClass().getLogger()
    request.cls.log = log
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # chrome_service = Service("C:/3.Softwares/SeleniumDrivers/chromedriver.exe")
        # browser_driver = webdriver.Chrome(service =chrome_service)
        browser_driver = webdriver.Chrome()
    elif browser_name == "edge":
        #edge_service = Service("C:/3.Softwares/SeleniumDrivers/chromedriver.exe")
        browser_driver = webdriver.Edge()

    browser_driver.implicitly_wait(10)
    browser_driver.maximize_window()
    browser_driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = browser_driver
    yield
    browser_driver.close()
    log = None






@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield

    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail)  or (report.passed) :
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        browser_driver.get_screenshot_as_file(name)

