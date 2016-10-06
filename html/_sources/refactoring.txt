###########
Refactoring
###########

Our last test passed, but unfortunately the method used to generate the html is cumbersome and just not good. Since we are using Django we want to be able to use its templating system to generate web pages for us. For us to accomplish this we are going to have to refactor our code. We have to change the way our code handles html without changing its functionality. TDD also states that we shouldnt do any refactoring without tests, therefore we are fisrt going to run our last functional test and see if its still passing. If its passing we can go ahead an modify our functional test::


        def test_home_page_html(self):
            request = self.factory.get('/')                    
            response = Home.as_view()(request)
            self.assertEqual('home.html', response.template_name[0]) 
When we run our tests with Python manage.py test contacts we get an error like the one below::



        Traceback (most recent call last):
            File "/home/hamub/projects/tdd_tutorial/addressbook/contacts/tests.py", line 14, in test_home_page_html
             response = Home.as_view()(request)
        NameError: name 'Home' is not defined
We then start the unittest-code  cycle again to make our tests pass. In this case reading the traceback we can find out that "home" is not defined as we have not imported it.Let us change home to Home in the import statements. When we run our tests again we see that there is another error::


        ImportError: Failed to import test module: contacts.testsTraceback (most recent call last):  File "/usr/lib/pyt

        hon3.5/unittest/loader.py", line 428, in _find_test_path    module = s
        elf._get_module_from_name(name)  File "/usr/lib/python3.5/unittest/loa
        der.py", line 369, in _get_module_from_name    __import__(name)  File

         "/home/hamub/projects/tdd_tutorial/addressbook/contacts/tests.py", line 4, in <module>    
         from .views import HomeImportError: cannot import name   'Home'

This is because we have not yet changed our view function to be a class based one. Let us quickly change our view function to use django`s generic class based views, by implemanting the following code in our views.py dont forget to import TemplateView from django.views::


         class Home(TemplateView):
             template_name = 'home.html'
         
We run our tests again, they seem to pass. But let us check with our functional tests to see if they are passing, by going to the terminal and running python acceptance.py. After the test we should see the following error::



        Traceback (most recent call last):  
          File "acceptance.py", line 19, in test_django_page('h1').textAssertionError: 
        False is not true

s is beacause we have not created any templates. But if we look closely at the tracebacks when we manually open the browser we see that there is a problem with our urls.py . Let us quicly alter everything since we are now using class based views. Let us quicly create a directory called templates inside our contacts directory and inside templates create a template called "home.html" and in that file we put the following markup::







