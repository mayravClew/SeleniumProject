from typing import Tuple, Union

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Chrome, Edge, Firefox
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import (
    StaleElementReferenceException,
)
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Wrapper for selenium operations."""

    def __init__(self, driver: Union[Chrome, Firefox, Edge]):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click(self, locator: Tuple[str, str]) -> None:
        el: WebElement = self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )
        el.click()

    def fill_text(self, locator: Tuple[str, str], txt: str) -> None:
        el: WebElement = self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )
        el.clear()
        el.send_keys(txt)

    def clear_text(self, locator: Tuple[str, str]) -> None:
        el: WebElement = self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )
        el.clear()


    def get_text(self, locator: Tuple[str, str]) -> str:
        el: WebElement = self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )
        # self._highlight_element(el, "green")
        return el.text

    def move_to_element(self, webelement: WebElement) -> None:
        action = ActionChains(self.driver)
        self.wait.until(expected_conditions.visibility_of(webelement))
        action.move_to_element(webelement).perform()


    def is_elem_displayed(self, locator: Tuple[str, str]) -> bool:
        try:
            el: WebElement = self.wait.until(
                expected_conditions.element_to_be_clickable(locator)
            )
            return True
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False