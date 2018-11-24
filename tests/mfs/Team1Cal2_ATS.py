import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class team1cal2_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_cal2(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://127.0.0.1:8000/admin")
       assert "Logged In"
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/th/a").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
       time.sleep(3)
       elem = driver.find_element_by_id("id_name")
       elem.send_keys("Test Calendar Title")
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/p/a").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
       time.sleep(7)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()