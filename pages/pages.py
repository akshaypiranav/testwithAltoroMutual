from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_input = (By.ID, "uid")
        self.password_input = (By.ID, "passw")
        self.login_button = (By.NAME, "btnSubmit")
        self.greeting_text = (By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/div/h1")

class TransferFundsPage:
    #transfer Elements
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.transfer_funds_link = (By.ID, "MenuHyperLink3")
        self.to_account_dropdown = (By.ID, "toAccount")
        self.transfer_amount_input = (By.ID, "transferAmount")
        self.transfer_button = (By.ID, "transfer")
        self.success_message = (By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/div/form/table/tbody/tr[6]/td/span[1]/span[@style='color: Red']")


class RecentTransactionsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.recent_transactions_link = (By.ID, "MenuHyperLink2")
        self.header_text = (By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/div/h1")

class AccountHistoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.go_button = (By.ID, "btnGetAccount")
        self.header_text = (By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/div/h1")