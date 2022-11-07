import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage(self):
        driver.find_element(By.CSS_SELECTOR, 'body > div.block-wrapper.request > div > form > label:nth-child(1) > inputbody > div.block-wrapper.request > div > form > label:nth-child(1) > input')
