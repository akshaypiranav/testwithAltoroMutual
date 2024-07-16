import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))
from pages import LoginPage, TransferFundsPage, RecentTransactionsPage, AccountHistoryPage

@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.set_capability("acceptInsecureCerts", True)
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestSuites:
    def login(self):
        login_page = LoginPage(self.driver)
        self.driver.get("http://hard.altoromutual.com/login.jsp")
        self.driver.find_element(*login_page.username_input).send_keys("admin")
        self.driver.find_element(*login_page.password_input).send_keys("admin")
        self.driver.find_element(*login_page.login_button).click()

    @pytest.mark.bat
    def test_login(self):
        self.login()
        login_page = LoginPage(self.driver)
        greeting_text = self.driver.find_element(*login_page.greeting_text).text
        assert "Hello Admin User" in greeting_text

    @pytest.mark.bat
    def test_transfer_funds(self):
        self.login()
        transfer_page = TransferFundsPage(self.driver)
        self.driver.find_element(*transfer_page.transfer_funds_link).click()
        self.driver.find_element(*transfer_page.to_account_dropdown).send_keys("800001")
        self.driver.find_element(*transfer_page.transfer_amount_input).send_keys("100")
        self.driver.find_element(*transfer_page.transfer_button).click()
        success_message = self.driver.find_element(*transfer_page.success_message).text
        assert "100.0 was successfully transferred from Account 800000 into Account 800001" in success_message

    @pytest.mark.sanity
    def test_recent_transactions(self):
        self.login()
        transactions_page = RecentTransactionsPage(self.driver)
        self.driver.find_element(*transactions_page.recent_transactions_link).click()
        assert "Recent Transactions" in self.driver.find_element(*transactions_page.header_text).text

    @pytest.mark.sanity
    def test_account_history(self):
        self.login()
        account_history_page = AccountHistoryPage(self.driver)
        self.driver.find_element(*account_history_page.go_button).click()
        assert "Account History - 800000 Corporate" in self.driver.find_element(*account_history_page.header_text).text
