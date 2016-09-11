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
<<<<<<< Updated upstream
=======
to resolve this we start a django project with the following command in the terminal::
        
        django-admin startproject addressbook .
This command tells django to create a project in the current directory as shown by the period(.).

Now when we run the acceptance test again with::
>>>>>>> Stashed changes

        python acceptance.py
we should get no output meaning that our acceptance test passed and therefore django is up and running
