import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
import sys


class test_1(unittest.TestCase):
    
        driver = webdriver.Chrome()
        driver.get("http://www.google.pl")
        print(driver.title)
        x=driver.find_elements_by_css_selector(input[id^='g'])
        print(x)
        x.send_keys("kutas")
        x.send_keys(Keys.RETURN)
        

        x= driver.find_element_by_css_selector("#tsf > div.tsf-p > div.jsb > center > input[type='submit']:nth-child(1)")

        x.click()
        x.submit()
        time.sleep(3)
        assert "Tibia" in driver.page_source
unittest.main()
