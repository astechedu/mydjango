
# Using Django inside a Python virtual environment

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4IRLqukJCFc6FR9kERu_1npoxO9XjVA8orNHsfTTZih7x5V05CIRiTeLpGBKEmL_ezGw&usqp=CAU">


Installing the virtual environment software


### Ubuntu virtual environment setup

	sudo pip3 install virtualenvwrapper


### macOS virtual environment setup

	sudo pip3 install virtualenvwrapper


### Windows 10 virtual environment setup

	pip3 install virtualenvwrapper-win

# Creating a virtual environment

	mkvirtualenv my_django_environment

  Showing: 

    (my_django_environment) ubuntu@ubuntu:~$

  deactivate — Exit out of the current Python virtual environment <br>
  workon — List available virtual environments <br>
  workon name_of_environment — Activate the specified Python virtual environment <br>
  rmvirtualenv name_of_environment — Remove the specified environment.


# Installing Django

nce you've created a virtual environment, and called workon to enter it, you can use pip3 to install Django.

	pip3 install django~=3.1

You can test that Django is installed by running the following command (this just tests that Python can find the Django module):

# Linux/macOS

	python3 -m django --version
	 3.1.2

# Windows

	py -3 -m django --version
	 3.1.2


Note: If the above Windows command does not show a django module present, try:

	py -m django --version


# Testing your installation

	mkdir django_test

	cd django_test	

	django-admin startproject mytestsite

	cd mytestsite

We can run the development web server from within this folder using manage.py and the runserver command, as shown.

	$ python3 manage.py runserver

Once the server is running you can view the site by navigating to the following URL on your local web browser: http://127.0.0.1:8000/


Changing the port

	$ python manage.py runserver 8080



Let’s look at what startproject created:

	mysite/
	    manage.py
	    mysite/
	        __init__.py
	        settings.py
	        urls.py
	        asgi.py
	        wsgi.py

<img src="https://learndjango.com/static/images/django31_welcome.png" width="500">



:+1: