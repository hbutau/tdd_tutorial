from selenium import webdriver

driver = webdriver.Chrome()
driver.get("localhost:8000")
assert "Django" in driver.title
driver.quit()
