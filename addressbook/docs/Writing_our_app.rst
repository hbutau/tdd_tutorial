##################################################
Creating the Addressbook Application with unittest
##################################################

Our last functional test failed as it couldnt find our expected heading. It is time we started thinking and planning how to make the functional test pass. We can do this by writting some code to make it pass. But before we can do that, the tenets of TDD dictate that before we write any production code we must write unittest first. Therefore we are going to write tests followed by our code and then we run our unitest followed by functional test to check if it is now passing. Let us start by creating our django app::

        python manage.py startapp contacts
The above command starts a django application inside our project directory. It also creates extra files which include a tests.py module for our application. It is in this file that we aregoing to write our unittest going forward. Let us open this file and enter the following code::



                class HomePageTest(TestCase):
                    
                    def setUp(self):                                                         
                        self.factory = RequestFactory()
                    
                    def test_home_page_html(self):
                        request = self.factory.get(reverse('home-page'))
                        response = home(request)
                        self.assertIn(b'<h1>Welcome to Addressbook</h1>', response.content)  

lets us run our test runner with::


                python manage.py test contacts
                
We should get the following failure::


                ======================================================================
ERROR: contacts.tests (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: contacts.tests
Traceback (most recent call last):
  File "/usr/lib/python3.5/unittest/loader.py", line 428, in _find_test_path
    module = self._get_module_from_name(name)
  File "/usr/lib/python3.5/unittest/loader.py", line 369, in _get_module_from_name
    __import__(name)
  File "/home/hamub/projects/tdd_tutorial/addressbook/contacts/tests.py", line 4, in <module>
    from .views import home
ImportError: cannot import name 'home'


----------------------------------------------------------------------
Ran 1 test in 0.001s

The test has failed because we do not have a home view as yet. Lets open views.py and write our first view function::


                from django.shortcuts import render
                from django.http import HttpResponse

                # Create your views here.

                def home():
                    pass
                    
when we run our test runner again we should see the following failure again:

ERROR: test_home_page_html (contacts.tests.HomePageTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/hamub/projects/tdd_tutorial/addressbook/contacts/tests.py", line 13, in test_home_page_html
    request = self.factory.get(reverse('home-page'))
  File "/home/hamub/.virtualenvs/tdd/lib/python3.5/site-packages/django/core/urlresolvers.py", line 578, in reverse
    return force_text(iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs)))
  File "/home/hamub/.virtualenvs/tdd/lib/python3.5/site-packages/django/core/urlresolvers.py", line 495, in _reverse_with_prefix
    (lookup_view_s, args, kwargs, len(patterns), patterns))
django.core.urlresolvers.NoReverseMatch: Reverse for 'home-page' with arguments '()' and keyword arguments '{}' not found. 0 pattern(s) tried: []

The reason we are getting this failure is because we have not defined any urls, lets go ahead and create one for our home page::


                from django.conf.urls import include, url
                from django.contrib import admin
                import contacts.views

                urlpatterns = [
                        url(r'^$', contacts.views.home, name='home-page',),
                        url(r'^admin/', include(admin.site.urls)),
                ]
Let us run our tests again and see if they fail again. After we run our test we get another failure:

======================================================================
ERROR: test_home_page_html (contacts.tests.HomePageTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/hamub/projects/tdd_tutorial/addressbook/contacts/tests.py", line 14, in test_home_page_html
    response = home(request)
TypeError: home() takes 0 positional arguments but 1 was given

----------------------------------------------------------------------
Ran 1 test in 0.012s

Our traceback is telling us there is something wrong with our view function. Lets us open up views.py and edit it::


                def home(request):
                    return HttpResponse('<h1>Welcome to Addressbook</h1>')



Finally our test passes with the following output:

(tdd) ~/projects/tdd_tutorial/addressbook (master) $ python manage.py test contacts
Creating test database for alias 'default'...
.
----------------------------------------------------------------------
Ran 1 test in 0.009s

OK
Destroying test database for alias 'default'...   


And finally we run our acceptance test with::


                python acceptance.py
                
It should pass and now we have a view that displays welcome to addressbook.


