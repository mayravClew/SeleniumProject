import json
import os
import socket

from model.login_model import User
from pages.login_page import LoginPage


users = ("john_doe@company.con", "123456")


class TestLogin():

    def __init__(self, driver):
        self.driver = driver

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        self.compare(True, login_page.login(User(*users)), "Login failed", "Login was successfull")

    def compare(self, expected, actual, error_text=None, success_text=None):
        if expected != actual:
            message = "value should be {} but was {}. {}".format(expected, actual, error_text)
            error_success
            raise Exception(message)
        print(success_text)