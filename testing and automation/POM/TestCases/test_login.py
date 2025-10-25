import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "loclahost:8000"
    username="test@email.com"
    password="123"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Title":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)