#################
Installing Django
#################

Firstly we write an acceptance test to check if django is running with the following code::

        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get("localhost:8000")
        assert "Django" in driver.title
If you went through the Django tutorial you should alraedy know that running the django develpment. this should give us the following error::

        (tdd) ~/projects/tdd_tutorial/addressbook (master)

        $ python acceptance.py
        Traceback (most recent call last):  Fil
        e "acceptance.py", line 5, in <module>
        assert 'Django' in driver.title AssertionError
to resolve this we start a django project with the following command in the terminal::
        
        django-admin startproject addressbook .
This command tells django to create a project in the current directory as shown by the period(.).

Now when we run the acceptance test again with::

        python acceptance.py
we should get no output meaning that our acceptance test passed and therefore django is up and running. Now that our functional test has led us to starting a django project we need to tweak it by changing it so that it uses the Python Standard stanard library unittest for testing. We want it to at least give us some information whether the test failed or passed. Lets open up acceptance.py with a text editor of our choice and add the following code::

        from selenium import webdriver
        import unittest


        Class Django_Page_Test(unittest.TestCase):
            
            def setUp(self):
                self.driver = webdriver.Firefox()

            def teardown(self):
                self.driver.quit()

            def test_django_page(self):
                self.assertEquals('Congratulations on your first Django-powered page.', self.driver.find_element_by_tag_name('h1'.text))
