import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time

def fun_1(unittest.TestCase):
	driver = webdriver.Chrome()
	driver.get("http://store.steampowered.com/")
	x= driver.find_element_by_name("term")
	x_send.keys(Keys.RETURN)
	time.sleep(3)


