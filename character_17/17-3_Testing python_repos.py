""" In python_repos.py, we printed the value of status_code to make sure the API
 call was successful. Write a program called test_python_repos.py that uses 
 pytest to assert that the value of status_code is 200. Figure out some other 
 assertions you can make: for example, that the number of items returned is 
 expected and that the total number of repositories is greater than a certain 
 amount. """


# Different response are not errors. It's not fit to pytest.