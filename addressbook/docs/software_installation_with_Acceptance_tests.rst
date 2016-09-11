#################
Installing Django
#################

Firstly we write an acceptance test to check if django is running with the following code::

        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get("localhost:8000")
        assert "Django" in driver.title
If you went through the Django tutorial you should alraedy know that running the django develpment. this should give us the following error::

        (tdd) ~/projects/tdd_tutorial/addressbook (master) $ python acceptance.pyTraceback (most recent call last):  File "accepta

        nce.py", line 5, in <module>    assert 'Django' in driver.titleAssert

        ionError

