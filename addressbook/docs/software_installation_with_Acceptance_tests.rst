#################
Installing Django
#################

Firstly we write an acceptance test to check if django is running with the following code::

        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get("localhost:8000")
        assert "Django" in driver.title
