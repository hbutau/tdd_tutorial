##################################################
Creating the Addressbook Application with unittest
##################################################

Our last functional test failed as it couldnt find our expected heading. It is time we started thinking and planning how to make the functional test pass. We can do this by writting some code to make it pass. But before we can do that, the tenets of TDD dictate that before we write any production code we must write unittest first. Therefore we are going to write tests followed by our code and then we run our unitest followed by functional test to check if it is now passing. Let us start by creating our django app::

        python manage.py startapp contacts
The above command starts a django application inside our project directory. It also creates extra files which include a tests.py module for our application. It is in this file that we aregoing to write our unittest going forward.
