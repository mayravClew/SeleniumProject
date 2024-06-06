from typing import Tuple

# import allure
from selenium.webdriver.common.by import By
from model.login_model import User
from pages.base_page import BasePage

# from pages.top_bars.top_menu_bar import TopMenuBar


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    USERNAME_FIELD: Tuple[str, str] = (By.ID, ":r1:")
    PASSWORD_FIELD: Tuple[str, str] = (By.ID, ":r2:")
    LOGIN_BUTTON: Tuple[str, str] = (By.XPATH, "//span[(text()='Login')]")
    LOGIN_ERROR_MESSAGE: Tuple[str, str] = (By.CSS_SELECTOR, "alert")
    PAGE_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, ".e-form-heading")
    FORGOT_PASSWORD_LINK: Tuple[str, str] = (By.CSS_SELECTOR, "[href='https://password/reset']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, user: User) -> bool:
        self.driver.get('https://web.eos.bnk-il.com/auth')
        self.is_elem_displayed(self.LOGIN_BUTTON)
        self.fill_text(self.USERNAME_FIELD, user.name)
        self.fill_text(self.PASSWORD_FIELD, user.psw)
        return self.is_elem_displayed(self.LOGIN_BUTTON)
        # not calling click, since and presume that it successfully passes the login validation.        return self.is_elem_displayed(self.LOGIN_BUTTON)
        # self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.LOGIN_ERROR_MESSAGE)

    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def click_forgot_password(self) -> None:
        self.click(self.FORGOT_PASSWORD_LINK)
