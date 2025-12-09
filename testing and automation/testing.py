import unittest
import pytest # when running -v is verbose -s disables output capture
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def add(a, b):
    return a + b

class TestMathOperation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1,1), 0)

if __name__ == "__main__":
    unittest.main()

def test_add():
    assert add(1,2) == 3
    assert add(-1 ,1) == 0

# fixture
@pytest.fixture
def sample_data():
    return {"a":1, "b":2}

def test_add(sample_data): 
    assert sample_data["a"] + sample_data["b"] == 3

# parameterization
def test_add(a, b, expected):
    assert add(a, b) == expected

# selenium end to end testing
driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python testing")
search_box.send_keys(Keys.RETURN)

assert "Python testing" in driver.title

driver.quit()