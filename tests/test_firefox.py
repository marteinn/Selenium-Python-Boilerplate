import unittest
from selenium import webdriver


class TestFirefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_title(self):
        self.driver.get("http://tomwaits.com")
        self.assertEquals("Tom Waits", self.driver.title)

    def test_url(self):
        self.driver.get("http://tomwaits.com")
        self.assertEquals(self.driver.current_url, "http://tomwaits.com/")

    def tearDown(self):
        self.driver.quit()
