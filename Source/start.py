from Source.tests.login_test import TestLogin
from Source.selenium_interface import SeleniumInterface

def main():
    print("Start main")
    selenium_interface = SeleniumInterface()
    login_test = TestLogin(selenium_interface.driver)
    login_test.test_valid_login()


if __name__ == "__main__":
    main()