# BusinessEssayWebsite

Website created using Django that displays an essay for my Business History module in different pages.

To use:


Python is required to run Django, to check if your system has Python installed, run this command in the command prompt:
  python --version

You will then get a result with a version number, for example 'Python 3.9.2'. If you do not have Python installed, you can install it from https://www.python.org/

To install Django, you must use a package manager like PIP which should be included in your python installation, to check you have PIP installed, run the following command:
  pip --version

You will then get a result such as 'pip 20.2.3 from c:\python39\lib\site-packages\pip (python 3.9)'. If you do not have PIP installed, you can install it from https://pypi.org/project/pip/


Install Django onto your computer by opening your terminal:
  For Linux/Mac:
    python -m pip install Django
  For Windows:
    py -m pip install Django
    
You can check if Django is installed by asking for its version number like this:
  django-admin --version
  
Now that Django is installed, download the folder found in the repository and make sure it is in a location you can easily access.
In your command prompt, navigate your directory to the first 'essay2' folder:
  For example:
    cd C:\Users\Taariq\Documents\BusinessEssayWebsite-main\essay2
Then, run the following command: (py for Windows, python for Linux/Mac)
  py or python manage.py runserver
You will then see a result like this:
  Performing system checks...

  System check identified no issues (0 silenced).
  April 10, 2023 - 16:17:54
  Django version 4.1.7, using settings 'essay2.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  
Copy the url given ( http://127.0.0.1:8000/ ) and add homepage (so url is now http://127.0.0.1:8000/homepage) into your preferred web browser and you will see the website.
