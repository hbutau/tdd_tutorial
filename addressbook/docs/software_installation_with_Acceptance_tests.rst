#################
Installing Django
#################

Firstly we write an acceptance test to check if django is running with the following code::

        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get("localhost:8000")
        assert "Django" in driver.title
If you went through the Django tutorial you should already know that running the django develpment. this should give us the following error::

        (tdd) ~/projects/tdd_tutorial/addressbook (master)

        $ python acceptance.py
        Traceback (most recent call last):  Fil
        e "acceptance.py", line 5, in <module>

        assert 'Django' in driver.title AssertionError
to resolve this we start a django project with the following command in the terminal::
        

        django-admin startproject addressbook .

This command tells django to create a project in the current directory as shown by the period(.).

Now when we run the acceptance test again with:
:

        python acceptance.py
we shoul
d get no output meaning that our acceptance test passed and therefore django is up and running. Now that our functional test has led us to starting a django project we need to tweak it by changing it so that it uses the Python Standard stanard library unittest for testing. We want it to at least give us some information whether the test failed or passed. Lets open up acceptance.py with a text editor of our choice and add the following code::

        from selenium import webdriver
        import unittest


        Class Django_Page_Test(unittest.TestCase):
            
            def setUp(self):
                self.driver = webdriver.Firefox()
                self.driver.get('localhost:8000')

            def teardown(self):
                self.driver.quit()

            def test_django_page(self):
                self.assertEquals('Congratulations on your first Django-powered page.', self.driver.find_element_by_tag_name('h1'.text)

Now that we have a passing unittest we want to write a functional test . Functional tests or end-to-end tests are used for checking the overall functionality of our programmes. Whilst unittest test the program form inside from the programmer`s point of view. All our coding should be inspired firstly by functional test, followed by the smallest amount of code that we can to make the test pass. After that we unittest our code and if it passes we refactor if necessary, otherwise we go back to unitesting. Since the last test we wrote passed why not write a functional test to che whether our webpage returns the correct html. Let us open our text editors and write the following code::

        #!/usr/bin/env python3     
        import unittest                 
        from selenium import webdrive

        class Django_Page_Test(unittest.TestCase):
            
            def setUp(self): 
                self.driver = webdriver.Chrome()                       
                self.driver.get('localhost:8000')     
            
            def tearDown(self):
                self.driver.quit() 
                
            def test_django_page(self):   
                self.assertTrue('Welcome to Adressbook' == self.driver.find_element_by_tag_name('h1').text)                                                               
        if __name__ == '__main__':                   
            unittest.main()        



if we run our functional test with::

        python acceptance.py

we should see the foolowing error::
        
        
        ======================================================================
        FAIL: test_django_page (acceptance.Django_Page_Test)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
        File "/home/hamub/projects/tdd_tutorial/addressbook/acceptance.py", line 17, in test_django_page
        self.assertTrue('Welcome to Adressbook' == self.driver.find_element_by_tag_name('h1').text)
        AssertionError: False is not true

        ----------------------------------------------------------------------

Now that we have have a failing test which expected our home page to specify that there should be a heading mentioning Welcome to Addressbook, it is time we start writing our unittest and production code for this test to pass.
        





        
