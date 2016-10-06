####################
Is Django Installed?
####################
In TDD the first step is always to write a failing test. We are going to use Selenium to check if Django is up and running by writting a test that will check whether we have the correct html in the page that is rendered by the development server. We start by writting  a failing  acceptance test to check if django is running with the following code::

        
        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get("localhost:8000")
        assert "It worked!" in driver.find_element_by_tag_name('h1').text
If you went through the Django tutorial you should already know that running the django develpment server, opening http://localhost:8000 should have a page with a heading that says "It worked!" . this should give us the following error if django is not installed or running properly::

        
        $ python acceptance.py
        Traceback (most recent call last):  Fil
        e "acceptance.py", line 5, in <module>

        assert 'It worked!' in driver.find_element_by_tag_name('h1').text 
        AssertionError
After  running our test and seeing it fail as expected the next step in TDD is to write the minimum amount of code to make our tests passs. In our case we can continue to install Django if we didnt and also start a django project. We start a django project with the following command in the terminal::
        

        django-admin startproject addressbook .

This command tells django to create a project in the current directory as shown by the period(.).

Now when we run the acceptance test again with::

        python acceptance.py
we should get no output meaning that our acceptance test passed and therefore django is up and running. Now that our functional test has led us to starting a django project we need to tweak it by changing it so that it uses the Python Standard  library unittest for testing. We want it to at least give us some information on how the test failed. 

##############################
Functional Tests with unittest
##############################
We are now going to use the standard python library`s unittest module in our acceptance test. In unit testing with unittest our test are encapsulated in Classes that inherit from TestCase. Our individual tests are then found in test methods that begin with test in their names so that they can be discovered and run by the test runner. We then have a number of functions to make assertions, like assertEqual, assertIn e.t.c. Lets open up acceptance.py with a text editor of our choice and add the following code::

        from selenium import webdriver
        import unittest


        Class Django_Page_Test(unittest.TestCase):
            
            def setUp(self):
                self.driver = webdriver.Firefox()
                self.driver.get('localhost:8000')

            def teardown(self):
                self.driver.quit()

            def test_django_page(self):
                self.assertEquals('It worked!', self.driver.find_element_by_tag_name('h1'.text)

Now that we have a passing unittest we want to write a functional test . Functional tests or end-to-end tests are used for checking the overall functionality of our programmes. Whilst unittest test the program form inside from the programmer`s point of view. All our coding should be inspired firstly by functional test, followed by the smallest amount of code that we can to make the test passes. After that we unittest our code and if it passes we refactor if necessary, otherwise we go back to unitesting. Since the last test we wrote passed why not write a functional test to check whether our webpage returns the expected html. Let us open our text editors and write the following code::

        #!/usr/bin/env python3     
        import unittest                 
        from selenium import webdriver

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

we should see the following error::
        
        
        
        Traceback (most recent call last):
        File "/home/hamub/projects/tdd_tutorial/addressbook/acceptance.py", line 17, in test_django_page
        self.assertTrue('Welcome to Adressbook' == self.driver.find_element_by_tag_name('h1').text)
        AssertionError: False is not true

        ----------------------------------------------------------------------

Now that we have have a failing test which expected our home page to specify that there should be a heading mentioning Welcome to Addressbook, it is time we start writing our unittest and production code for this test to pass.
        





        
